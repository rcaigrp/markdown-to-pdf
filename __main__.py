import sys
import json

sys.path.insert(0, '/workspace/projects/markdown_to_pdf')

from markdown_to_pdf.converter import convert_markdown_to_pdf
from markdown_to_pdf.config import load_config


def main():
    config = load_config()
    input_path = config['input_path']
    output_path = config['output_path']
    convert_markdown_to_pdf(input_path, output_path)


if __name__ == '__main__':
    main()
