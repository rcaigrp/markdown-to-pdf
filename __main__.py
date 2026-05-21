import json
from pathlib import Path
from markdown_to_pdf.converter import convert_md_to_html, html_to_pdf

def main():
    config_path = Path(__file__).parent / 'config.json'
    with open(config_path) as f:
        config = json.load(f)
    
    input_path = config['input_path']
    output_path = config['output_path']
    
    with open(input_path) as f:
        md_text = f.read()
    
    html_text = convert_md_to_html(md_text)
    html_to_pdf(html_text, output_path)

if __name__ == '__main__':
    main()
