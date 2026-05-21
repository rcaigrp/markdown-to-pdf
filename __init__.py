import markdown


def convert(markdown_text: str) -> str:
    """Convert a markdown string to an HTML string.

    Args:
        markdown_text: The markdown string to convert.

    Returns:
        The HTML string representation.
    """
    return markdown.markdown(markdown_text)
