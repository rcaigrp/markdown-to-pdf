import os
import pytest
from unittest.mock import patch, mock_open, MagicMock

def test_criterion_1_module_runs():
    assert os.path.exists('/workspace/projects/markdown_to_pdf/__main__.py')
    assert os.path.exists('/workspace/projects/markdown_to_pdf/__init__.py')

def test_criterion_2_reads_config():
    with patch('builtins.open', mock_open(read_data='{"input_path": "in.md", "output_path": "out.pdf"}')):
        with patch('json.load', return_value={'input_path': 'in.md', 'output_path': 'out.pdf'}):
            from markdown_to_pdf import __main__ as main_module
            assert hasattr(main_module, 'main')

def test_criterion_3_convert_md_to_html():
    import markdown
    assert '<h1>Hello</h1>' in markdown.markdown('# Hello')

def test_criterion_4_convert_html_to_pdf():
    with patch('markdown_to_pdf.converter.FPDF') as MockFPDF:
        mock_pdf = MagicMock()
        MockFPDF.return_value = mock_pdf
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf('<h1>Test</h1>', 'test.pdf')
        assert mock_pdf.add_page.called
        assert mock_pdf.html.called

def test_criterion_5_saves_pdf():
    with patch('markdown_to_pdf.converter.FPDF') as MockFPDF:
        mock_pdf = MagicMock()
        MockFPDF.return_value = mock_pdf
        from markdown_to_pdf.converter import html_to_pdf
        html_to_pdf('<h1>Test</h1>', 'test.pdf')
        assert mock_pdf.output.called
        assert mock_pdf.output.call_args.kwargs.get('dest') == 'F'

def test_criterion_6_valid_structure():
    assert os.path.exists('/workspace/projects/markdown_to_pdf/config.json')
    assert os.path.exists('/workspace/projects/markdown_to_pdf/converter.py')
