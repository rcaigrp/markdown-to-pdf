import json
import markdown
import os
from weasyprint import HTML

def load_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def convert():
    config = load_config()
    input_path = config['input_path']
    output_path = config['output_path']
    
    with open(input_path, 'r') as f:
        md_content = f.read()
        
    html_content = markdown.markdown(md_content)
    
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: sans-serif; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""
    
    html = HTML(string=full_html)
    html.write_pdf(output_path)
