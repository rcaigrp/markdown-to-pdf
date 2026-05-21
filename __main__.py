import json
import os
from markdown_to_pdf import convert_md_to_html, convert_html_to_pdf

def main():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    input_path = config['input']
    output_path = config['output']
    
    with open(input_path, 'r') as f:
        md_text = f.read()
    
    html_text = convert_md_to_html(md_text)
    convert_html_to_pdf(html_text, output_path)

if __name__ == '__main__':
    main()
