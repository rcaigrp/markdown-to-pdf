import markdown
from fpdf import FPDF

def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

def html_to_pdf(html, output_path):
    pdf = FPDF()
    pdf.add_html(html)
    pdf.output(output_path)

def convert_markdown_to_pdf(input_path, output_path):
    with open(input_path, 'r') as f:
        markdown_text = f.read()
    html = markdown_to_html(markdown_text)
    html_to_pdf(html, output_path)
