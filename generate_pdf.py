from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(150)
        self.cell(0, 10, 'ConsultBridge - Humanized Version', 0, 1, 'R')

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(150)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font('helvetica', size=11)

with open('ConsultBridge_Humanized.txt', 'r', encoding='utf-8') as f:
    for line in f:
        sanitized_line = line.replace('—', '--').replace('–', '-').replace('’', "'").replace('“', '"').replace('”', '"').replace('é', 'e')
        
        # Check if line looks like a major header to bold it
        if line.strip().isupper() and len(line.strip()) > 3 or line.strip().startswith('Table'):
            pdf.set_font('helvetica', 'B', 12)
            pdf.multi_cell(0, 6, sanitized_line)
            pdf.set_font('helvetica', '', 11)
        else:
            pdf.multi_cell(0, 6, sanitized_line)

pdf.output('ConsultBridge_Humanized.pdf')
