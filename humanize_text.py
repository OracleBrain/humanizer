import os
import argparse
try:
    from docx import Document
except ImportError:
    print("Please install python-docx: pip install python-docx")
    exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    exit(1)

def read_input(file_path):
    if file_path.endswith('.docx'):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

def save_output(text, output_path):
    # Depending on your PDF generation workflow, you might just want it as a text or markdown file.
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def humanize_text(text, api_key=None, model="gpt-4o"):
    """
    Calls the OpenAI API to humanize text.
    """
    client = OpenAI(api_key=api_key)

    system_prompt = (
        "You are an expert ghostwriter and humanizer. Your task is to rewrite the provided "
        "AI-generated text to make it sound 100% human, natural, engaging, and professional.\n\n"
        "Follow these strict rules:\n"
        "1. Remove all AI hallmarks and overused words (e.g., 'delve', 'crucial', 'furthermore', 'tapestry', 'testament to', 'landscape', 'moreover', 'pivotal').\n"
        "2. Break up long, convoluted sentences typical of AI generation.\n"
        "3. Use varied sentence lengths. Mix short, punchy sentences with longer ones naturally.\n"
        "4. Transition smoothly between thoughts without mechanical connectors (e.g., 'Firstly', 'In conclusion').\n"
        "5. Maintain the original core message, context, and any specific formatting (like bullet points or headings) so it can be inserted directly into a PDF/document.\n"
        "6. Do not include conversational padding like 'Here is the humanized text:'. Just output the final text."
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Please humanize the following text:\n\n{text}"}
        ],
        temperature=0.7, # Slightly higher temperature for more natural variance
    )
    
    return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Humanize AI text for PDF insertion.")
    parser.add_argument("input_file", help="Path to the input file (e.g., ConsultBridge.docx)")
    parser.add_argument("--output", help="Path to the output file (default: humanized_output.txt)", default="humanized_output.txt")
    parser.add_argument("--model", help="OpenAI model to use", default="gpt-4o")
    
    args = parser.parse_args()
    
    # Needs OPENAI_API_KEY set in environment
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Run: export OPENAI_API_KEY='your-key-here'")
        return

    print(f"Reading {args.input_file}...")
    try:
        text = read_input(args.input_file)
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    print(f"Humanizing text using {args.model}... (This may take a minute depending on length)")
    try:
        humanized = humanize_text(text, model=args.model)
    except Exception as e:
        print(f"Error during humanization: {e}")
        return

    print(f"Saving humanized text to {args.output}...")
    save_output(humanized, args.output)
    
    print("Done! The text is now perfectly humanized and ready to be inserted directly into your PDF workflow.")

if __name__ == "__main__":
    main()
