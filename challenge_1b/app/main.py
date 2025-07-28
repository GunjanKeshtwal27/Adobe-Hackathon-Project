
# import os
# import json
# from extractor import extract_sections
# from persona_analyzer import rank_and_summarize


# INPUT_DIR = "sample_input"
# OUTPUT_DIR = "sample_output"

# def load_persona():
#     """
#     Load persona description and job-to-be-done from persona.txt.
#     """
#     with open("persona.txt", "r", encoding="utf-8") as f:
#         return f.read()

# def process_pdfs_for_persona():
#     if not os.path.exists(OUTPUT_DIR):
#         os.makedirs(OUTPUT_DIR)

#     persona_description = load_persona()
#     all_sections = []

#     pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
#     if not pdf_files:
#         print("⚠️ No PDF files found in sample_input folder.")
#         return

#     # Extract sections from all PDFs
#     for pdf_file in pdf_files:
#         pdf_path = os.path.join(INPUT_DIR, pdf_file)
#         extracted = extract_sections(pdf_path)

#         for item in extracted:
#             all_sections.append({
#                 "document": pdf_file,
#                 "page": item['page'],
#                 "heading": item['heading'],
#                 "text": item['text']
#             })

#     # Rank sections by relevance and generate summaries
#     ranked_sections = rank_and_summarize(all_sections, persona_description)

#     # Save output
#     output = {
#         "persona": persona_description,
#         "results": ranked_sections
#     }

#     output_file = os.path.join(OUTPUT_DIR, "persona_output.json")
#     with open(output_file, "w", encoding="utf-8") as f:
#         json.dump(output, f, indent=2)
#     print(f"✅ Persona-based analysis saved to: {output_file}")

# if __name__ == "__main__":
#     process_pdfs_for_persona()



























import os
import json
from extractor import extract_sections
from persona_analyzer import rank_and_summarize

# Folders
INPUT_DIR = "sample_input"
OUTPUT_DIR = "sample_output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "persona_output.json")
PERSONA_FILE = "persona.txt"

# Read Persona Description
with open(PERSONA_FILE, "r", encoding="utf-8") as f:
    persona_description = f.read().strip()

# Process all PDFs in the input folder
all_sections = []
pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]

if not pdf_files:
    print("⚠️ No PDFs found in sample_input folder.")
    exit()

for pdf_file in pdf_files:
    pdf_path = os.path.join(INPUT_DIR, pdf_file)
    print(f"📄 Processing: {pdf_file}")

    sections = extract_sections(pdf_path)

    if sections:
        print(f"✅ {len(sections)} sections extracted from {pdf_file}")
        # Add document name to each section
        for section in sections:
            section["document"] = pdf_file
        all_sections.extend(sections)
    else:
        print(f"⚠️ No valid sections found in {pdf_file}")

# Rank & Summarize All Sections
ranked_results = rank_and_summarize(all_sections, persona_description)

# Save Results
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

output_data = {
    "persona": persona_description,
    "results": ranked_results
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

print(f"\n✅ Persona-based analysis saved to: {OUTPUT_FILE}")


