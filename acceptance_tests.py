import unittest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, '/workspace/projects/markdown_to_pdf')

class TestConverter(unittest.TestCase):
    @patch('markdown.markdown')
    def test_markdown_to_html(self, mock_md):
        from markdown_to_pdf.converter import markdown_to_html
        mock_md.return_value = "<html>Test</html>"
        result = markdown_to_html("# Test")
        self.assertEqual(result, "<html>Test</html>")

    @patch('markdown_to_pdf.converter.FPDF')
    def test_html_to_pdf(self, mock_fpdf_class):
        from markdown_to_pdf.converter import html_to_pdf
        mock_pdf = MagicMock()
        mock_fpdf_class.return_value = mock_pdf
        html_to_pdf("<html>Test</html>", "out.pdf")
        mock_pdf.add_html.assert_called_once_with("<html>Test</html>")
        mock_pdf.output.assert_called_once_with("out.pdf")

    @patch('markdown_to_pdf.converter.markdown')
    @patch('markdown_to_pdf.converter.FPDF')
    def test_convert_markdown_to_pdf(self, mock_fpdf_class, mock_md):
        from markdown_to_pdf.converter import convert_markdown_to_pdf
        
        with open("/tmp/test_input.md", "w") as f:
            f.write("# Hello")
        
        mock_md.markdown.return_value = "<h1>Hello</h1>"
        mock_pdf = MagicMock()
        mock_fpdf_class.return_value = mock_pdf
        
        convert_markdown_to_pdf("/tmp/test_input.md", "/tmp/test_output.pdf")
        
        mock_pdf.add_html.assert_called_once()
        mock_pdf.output.assert_called_once_with("/tmp/test_output.pdf")
