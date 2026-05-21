import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_criterion_1_module_import():
    try:
        import markdown_to_pdf
        assert True
    except ImportError:
        pytest.fail("Failed to import markdown_to_pdf module")

def test_criterion_2_convert_function():
    from markdown_to_pdf import convert
    assert callable(convert)
    result = convert("# Hello")
    assert isinstance(result, str)
    assert "<h1>" in result or "<h2>" in result
