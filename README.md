# AI Text Humanizer & Document Generator

Hey there! 👋 Welcome to the **AI Text Humanizer**. 

Ever generated some awesome content with AI, only to realize it sounds a bit... well, robotic? We've all been there—reading words like "delve," "testament to," or "moreover" and instantly knowing a machine wrote it. 

That's exactly what this project fixes. It takes your AI-generated text and gives it a warm, natural, and genuinely human voice. Plus, it can instantly turn your newly humanized text into a clean, professional PDF.

## What's Inside?

This repo contains two main scripts that work together seamlessly:

1. **`humanize_text.py`**: The brains of the operation. It reads your document (either `.txt` or `.docx`), chats with OpenAI's `gpt-4o` model, and rewrites the text. It strips away all the typical AI jargon, varies sentence lengths, and makes the flow feel like it was written by an expert copywriter.
2. **`generate_pdf.py`**: The finishing touch. Once your text is polished, this script takes the humanized output and formats it nicely into a ready-to-share PDF document.

## Getting Started

Ready to give your text a human touch? Here's how to get up and running.

### 1. Install the Requirements

You'll need a few Python packages to get started. Open up your terminal and install them:

```bash
pip install openai python-docx fpdf
```

### 2. Add Your API Key

Since we're using OpenAI to do the heavy lifting, you'll need to set your API key as an environment variable. 

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### 3. Run the Humanizer

Got a document ready? Run the script and watch the magic happen. You can pass in a plain text file or a Word document.

```bash
python humanize_text.py input_document.docx --output humanized_output.txt
```
*(By default, it uses `gpt-4o`, but you can specify a different model using the `--model` flag if you prefer!)*

### 4. Create Your PDF

Once you're happy with the `humanized_output.txt` (or in the default case, `ConsultBridge_Humanized.txt`), you can turn it into a shiny new PDF. The `generate_pdf.py` script looks for `ConsultBridge_Humanized.txt` by default, but you can easily adapt it for your own file names:

```bash
python generate_pdf.py
```

Boom. You've got a beautifully formatted, completely human-sounding document ready to go.

## Why This Project?

Because communication should sound like people talking to people. Whether you're drafting a report, writing an article, or preparing a presentation, your words shouldn't scream "I used an AI to write this." 

Feel free to fork, tweak, and use this workflow to make your own writing shine. If you run into any issues or have cool ideas for improvements, don't hesitate to reach out or drop a pull request!

Happy writing! ✍️