import markdown

def convert(md_content):
    """
    Converts a Markdown string to an HTML string.
    """
    html = markdown.markdown(md_content)
    return html