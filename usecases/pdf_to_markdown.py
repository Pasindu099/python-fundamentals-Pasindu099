import pdfplumber
import os


def pdf_to_markdown(pdf_path: str) -> str:
    """Extract text from a PDF file and format it as Markdown."""
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return ""

    text_content = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text() or ""
                text_content.append(f"### Page {i}\n\n{page_text}\n")
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

    markdown_text = "\n".join(text_content)
    return markdown_text
