# Adobe-Hackathon-Project
This repository contains the solution for the Adobe India Hackathon 2025 – Connecting the Dots challenge.

#  Smart  Companion – Adobe India Hackathon

This project is built for the Adobe India Hackathon challenge to help  developers in quickly analyze long technical documents using Generative AI and NLP.

---

##  Problem Statement Breakdown

### Round 1A – Extract Document Outline

- Parse academic/research PDFs.
- Maintain semantic hierarchy.
- Automatically detect structured headings (H1, H2, H3).
- Output saved as: `sample_output/test.json`.

###  Round 1B – Persona-Based Analysis

- Accepts a **persona** and job-to-be-done input from a `persona.txt` file.
- Uses **semantic search** to rank sections of a PDF that are most relevant.
- Generates intelligent summaries using Transformers (T5).
- Outputs: `sample_output/persona_output.json`.

---

##  Features

-  AI-Powered Topic Detection using Sentence Transformers.
-  PDF Parsing using PyMuPDF.
-  Persona-based relevance ranking.
-  Summarization with `transformers` (`t5-small`).
-  Supports **multiple PDFs** in batch mode.

---

##  Project Structure

Adobe_Hack/
- │
- ├── app/
- │ ├── main.py 
- │ ├── extractor.py # Extract heading and content
- │ ├── ml_model.py #  vectorizer + classifier
- │ ├── persona_analyzer.py # Persona-based ranking & summary
- │
- ├── sample_input/
- │ └── *.pdf #pdf files
- │
- ├── sample_output/
- │ ├── test.json
- │ └── persona_output.json
- │
- ├── persona.txt # Described user goal 
- └── requirements.txt # All required dependencies



---

##  Setup Instructions (without using Docker)

### 1. 🐍 Create Python Virtual Environment

 bash
 python -m venv venv

## 2.  Activate Virtual Environment

venv\Scripts\activate

## 3.  Install Dependencies

pip install -r requirements.txt

## 4.  Running the Project
python app/main.py 


##  Example output - test.json

<img width="1496" height="219" alt="image" src="https://github.com/user-attachments/assets/4786b8bb-76b9-4a39-a632-19a828618398" />

## Technologies used-
-Python 3.10

-PyMuPDF (fitz)

-SentenceTransformers

-Transformers (t5-small)

-scikit-learn, joblib

-tqdm, json, argparse






