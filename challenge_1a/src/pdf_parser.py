import fitz  # PyMuPDF library

class PDFParser:
    def __init__(self, pdf_path):
        """
        Initializes the PDFParser with the path to the PDF file.
        """
        self.pdf_path = pdf_path
        self.document = fitz.open(pdf_path)

    def extract_text_with_properties(self):
        """
        Extracts text along with its properties (font size, font name, page number) from the PDF.
        """
        extracted_data = []
        for page_num in range(self.document.page_count):
            page = self.document.load_page(page_num)
            # Extract detailed text information using the 'textpage' object
            text_blocks = page.get_text("dict")["blocks"]

            for block in text_blocks:
                if block["type"] == 0:  # This is a text block
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            if text:  # Skip empty strings
                                extracted_data.append({
                                    "text": text,
                                    "font_size": span["size"],
                                    "font_name": span["font"],
                                    "is_bold": "bold" in span["font"].lower(), # Heuristic to detect boldness
                                    "page": page_num + 1  # Page numbers are 1-based
                                })
        return extracted_data

    def close(self):
        """
        Closes the PDF document.
        """
        self.document.close()

