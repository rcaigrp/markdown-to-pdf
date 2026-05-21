import os
import json
import re
import markdown
from fpdf import FPDF


def html_to_pdf(html: str, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    # Strip HTML tags to extract plain text for PDF
    text = re.sub(r'<[^>]*>', '', html)
    pdf.multi_cell(0, 10, text)
    pdf.output(output_path, "F")


def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    input_path = config["input_path"]
    output_path = config["output_path"]

    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown.markdown(md_text)
    html_to_pdf(html, output_path)
    print(f"PDF saved to {output_path}")


if __name__ == "__main__":
    main()
