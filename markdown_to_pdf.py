import markdown
import html2pdf

def convert_md_to_html(md_text):
    return markdown.markdown(md_text)

def convert_html_to_pdf(html_text, output_path):
    html2pdf.html2pdf(html=html_text, output=output_path)
