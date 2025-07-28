import os
import json
from pdf_parser import PDFParser
from outline_generator import OutlineGenerator

def process_pdf(input_pdf_path, output_json_path):
    """
    Processes a single PDF file and generates a JSON outline file.
    """
    print(f"Processing PDF: {input_pdf_path}")
    parser = PDFParser(input_pdf_path)
    extracted_data = parser.extract_text_with_properties()
    parser.close()

    generator = OutlineGenerator()
    outline_data = generator.generate_outline(extracted_data)

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(outline_data, f, ensure_ascii=False, indent=2)
    print(f"Generated outline: {output_json_path}")

if __name__ == "__main__":
    input_dir = "../input"
    output_dir = "../output"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process all PDF files found in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            input_pdf_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_json_path = os.path.join(output_dir, output_filename)
            process_pdf(input_pdf_path, output_json_path)

