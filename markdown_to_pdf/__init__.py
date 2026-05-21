import markdown

def convert(md_text: str) -> str:
    """Converts Markdown text to HTML."""
    return markdown.markdown(md_text)
