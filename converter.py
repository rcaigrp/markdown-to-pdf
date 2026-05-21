import markdown
from fpdf import FPDF

def convert_md_to_html(md_text):
    return markdown.markdown(md_text)

def html_to_pdf(html_text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.html(html_text, x=0, y=0)
    pdf.output(dest='F', filename=output_path)
