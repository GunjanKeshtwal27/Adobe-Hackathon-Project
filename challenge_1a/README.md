# Adobe India Hackathon - Connecting the Dots Challenge (Round 1A)

## PDF Outline Extractor

This project is a solution for Round 1A of the Adobe India Hackathon's "Connecting the Dots" Challenge. Its purpose is to extract the Title and headings (H1, H2, H3) from a PDF file and output them in a structured JSON format.

## Approach

Our solution utilizes the `PyMuPDF` library to parse PDFs, extract text and font properties, and then analyze these properties to identify headings. The hierarchy of headings is inferred based on font size and boldness.

**Key Steps:**

1.  **PDF Parsing:** Use `PyMuPDF` to extract text, font size, font name, and page number for each text span in the PDF.
2.  **Font Size Analysis:** Analyze the font sizes of the extracted text to identify potential title and heading sizes. This is a heuristic approach where the largest font is considered the title, the next largest as H1, and so on.
3.  **Heading Identification:** Identify headings by combining font size and boldness cues.
4.  **JSON Output:** Structure the identified title and headings into the specified JSON format.

## Libraries Used

*   **PyMuPDF (fitz):** For PDF parsing and text extraction.
*   **json:** Python's built-in module for handling JSON files.

## How to Build and Run Your Solution

This solution is containerized using Docker.

**1. Build the Docker Image:**

Ensure you have Docker installed. Then, navigate to the root directory of your project (where the `Dockerfile` is located) and run the following command:

```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .