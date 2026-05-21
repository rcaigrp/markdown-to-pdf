import sys
from markdown_to_pdf import convert

if __name__ == "__main__":
    text = sys.stdin.read()
    print(convert(text))
