
import fitz  # PyMuPDF

def extract_sections(pdf_path):
    """
    Extract meaningful headings and paragraphs from a PDF.
    Skips cover pages, citation blocks, and very short/irrelevant text.
    """
    doc = fitz.open(pdf_path)
    sections = []
    current_section = None

    for page_num, page in enumerate(doc):
        if page_num == 0:  # 🚨 Skip cover/title page
            continue

        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()

            # 🚨 Skip empty lines, references, or citation-heavy text
            if (not text or
                len(text.split()) < 3 or
                text.lower().startswith("references") or
                text.startswith("[1]")):
                continue

            # 🚨 Skip all-lowercase lines (likely not headings)
            if text.islower():
                continue

            # Detect heading by font size
            font_size = block[3] - block[1]
            if font_size > 15:  # Likely H1
                if current_section and len(current_section["text"].split()) > 20:
                    sections.append(current_section)
                current_section = {
                    "heading": text,
                    "level": "H1",
                    "text": "",
                    "page": page_num + 1
                }
            elif font_size > 12:  # Likely H2
                if current_section and len(current_section["text"].split()) > 20:
                    sections.append(current_section)
                current_section = {
                    "heading": text,
                    "level": "H2",
                    "text": "",
                    "page": page_num + 1
                }
            else:
                if current_section:
                    current_section["text"] += text + " "

    # Add last section if valid
    if current_section and len(current_section["text"].split()) > 20:
        sections.append(current_section)

    return sections
