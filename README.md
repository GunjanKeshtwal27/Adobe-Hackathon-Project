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
-│
-├── app/
-│ ├── main.py 
-│ ├── extractor.py # Extract heading and content
-│ ├── ml_model.py #  vectorizer + classifier
-│ ├── persona_analyzer.py # Persona-based ranking & summary
-│
-├── sample_input/
-│ └── *.pdf #pdf files
-│
-├── sample_output/
-│ ├── test.json
-│ └── persona_output.json
-│
-├── persona.txt # Described user goal 
-└── requirements.txt # All required dependencies



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
{
  "title": "",
  "outline": [
    {
      "level": "H3",
      "text": "Welcome to the\u202f\u201cConnecting the Dots\u201d Challenge",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Rethink Reading. Rediscover Knowledge",
      "page": 2
    },
    {
      "level": "H2",
      "text": "The Journey Ahead",
      "page": 2
    },
    {
      "level": "H2",
      "text": "\u2022 Round 1:",
      "page": 2
    },
    {
      "level": "H2",
      "text": "\u2022 Round 2:",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Why This Matters",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Are you in?",
      "page": 2
    },
    {
      "level": "H2",
      "text": "Round 1A: Understand Your Document",
      "page": 3
    },
    {
      "level": "H3",
      "text": "Challenge Theme: Connecting the Dots Through Docs",
      "page": 3
    },
    {
      "level": "H1",
      "text": "Your Mission",
      "page": 3
    },
    {
      "level": "H2",
      "text": "Why This Matters",
      "page": 3
    },
    {
      "level": "H2",
      "text": "What You Need to Build",
      "page": 3
    },
    {
      "level": "H2",
      "text": "You must build a solution that:",
      "page": 3
    },
    {
      "level": "H3",
      "text": "\u2022 Accepts a PDF file (up to 50 pages)",
      "page": 3
    },
    {
      "level": "H1",
      "text": "\u2022 Extracts:",
      "page": 3
    },
    {
      "level": "H1",
      "text": "o Title",
      "page": 3
    },
    {
      "level": "H3",
      "text": "o Headings: H1, H2, H3 (with level and page number)",
      "page": 3
    },
    {
      "level": "H2",
      "text": "You Will Be Provided",
      "page": 3
    },
    {
      "level": "H2",
      "text": "3. Sample Dockerfile  \n4. Sample Solution",
      "page": 4
    },
    {
      "level": "H1",
      "text": "Docker Requirements",
      "page": 4
    },
    {
      "level": "H1",
      "text": "\u2022",
      "page": 4
    },
    {
      "level": "H2",
      "text": "\u2022 CPU architecture: amd64 (x86_64)",
      "page": 4
    },
    {
      "level": "H2",
      "text": "\u2022 No GPU dependencies",
      "page": 4
    },
    {
      "level": "H3",
      "text": "\u2022 Model size (if used) \u2264 200MB",
      "page": 4
    },
    {
      "level": "H3",
      "text": "\u2022 Should work offline \u2014 no network/internet calls",
      "page": 4
    },
    {
      "level": "H1",
      "text": "Expected Execution",
      "page": 4
    },
    {
      "level": "H3",
      "text": "We will build the docker image using the following command:",
      "page": 4
    },
    {
      "level": "H2",
      "text": "```docker build --platform linux/amd64 -t \nmysolutionname:somerandomidentifier```",
      "page": 4
    },
    {
      "level": "H3",
      "text": "```docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --\nnetwork none mysolutionname:somerandomidentifier```",
      "page": 4
    },
    {
      "level": "H2",
      "text": "Your container should:",
      "page": 4
    },
    {
      "level": "H1",
      "text": "\u2022 output.json",
      "page": 4
    },
    {
      "level": "H1",
      "text": "Constraints",
      "page": 4
    },
    {
      "level": "H2",
      "text": "Constraint  \nRequirement  \nExecution \ntime",
      "page": 4
    },
    {
      "level": "H3",
      "text": "\u2264 10 seconds for a 50-page \nPDF",
      "page": 4
    },
    {
      "level": "H2",
      "text": "Model size  \u2264 200MB (if used)",
      "page": 5
    },
    {
      "level": "H2",
      "text": "Network  \nNo internet access \nallowed",
      "page": 5
    },
    {
      "level": "H1",
      "text": "Runtime",
      "page": 5
    },
    {
      "level": "H1",
      "text": "Scoring Criteria",
      "page": 5
    },
    {
      "level": "H3",
      "text": "Criteria  \nMax \nPoints  \nHeading Detection Accuracy (Precision + \nRecall)  \n25",
      "page": 5
    },
    {
      "level": "H1",
      "text": "Total  \n45",
      "page": 5
    },
    {
      "level": "H1",
      "text": "Submission Checklist",
      "page": 5
    },
    {
      "level": "H2",
      "text": "o Your approach",
      "page": 5
    },
    {
      "level": "H2",
      "text": "o Any models or libraries used",
      "page": 5
    },
    {
      "level": "H1",
      "text": "Pro Tips",
      "page": 5
    },
    {
      "level": "H3",
      "text": "\u2022 Test your solution across both simple and complex PDFs.",
      "page": 5
    },
    {
      "level": "H2",
      "text": "What Not to Do",
      "page": 6
    },
    {
      "level": "H3",
      "text": "\u2022 Do not hardcode headings or file-specific logic",
      "page": 6
    },
    {
      "level": "H3",
      "text": "\u2022 Do not make API or web calls",
      "page": 6
    },
    {
      "level": "H3",
      "text": "\u2022 Do not exceed the runtime/model size constraints",
      "page": 6
    },
    {
      "level": "H2",
      "text": "[[Public Dataset Folder]]",
      "page": 6
    },
    {
      "level": "H3",
      "text": "(For Sample Input and Output Files, please refer to the appendix)",
      "page": 6
    },
    {
      "level": "H2",
      "text": "Round 1B: Persona-Driven Document Intelligence",
      "page": 7
    },
    {
      "level": "H3",
      "text": "Theme:\u202f\u201cConnect What Matters \u2014 For the User Who Matters\u201d",
      "page": 7
    },
    {
      "level": "H2",
      "text": "Challenge Brief (For Participants)",
      "page": 7
    },
    {
      "level": "H1",
      "text": "Input Specification",
      "page": 7
    },
    {
      "level": "H3",
      "text": "2. Document Collection: 3-10 related PDFs Persona Definition: Role",
      "page": 7
    },
    {
      "level": "H3",
      "text": "description with specific expertise and focus areas",
      "page": 7
    },
    {
      "level": "H3",
      "text": "3. Job-to-be-Done: Concrete task the persona needs to accomplish",
      "page": 7
    },
    {
      "level": "H2",
      "text": "Sample Test Cases",
      "page": 7
    },
    {
      "level": "H2",
      "text": "Test Case 1: Academic Research",
      "page": 7
    },
    {
      "level": "H3",
      "text": "\u2022 Persona: PhD Researcher in Computational Biology",
      "page": 7
    },
    {
      "level": "H2",
      "text": "Test Case 2: Business Analysis",
      "page": 8
    },
    {
      "level": "H3",
      "text": "\u2022 Documents: 3 annual reports from competing tech companies \n(2022-2024)",
      "page": 8
    },
    {
      "level": "H2",
      "text": "\u2022 Persona: Investment Analyst",
      "page": 8
    },
    {
      "level": "H3",
      "text": "\u2022 Job: \"Analyze revenue trends, R&D investments, and market \npositioning strategies\"",
      "page": 8
    },
    {
      "level": "H2",
      "text": "Test Case 3: Educational Content",
      "page": 8
    },
    {
      "level": "H3",
      "text": "\u2022 Documents: 5 chapters from organic chemistry textbooks",
      "page": 8
    },
    {
      "level": "H2",
      "text": "\u2022 Persona: Undergraduate Chemistry Student",
      "page": 8
    },
    {
      "level": "H1",
      "text": "Required Output",
      "page": 8
    },
    {
      "level": "H2",
      "text": "\u2022 Output JSON format: Refer challenge1b_output.json",
      "page": 8
    },
    {
      "level": "H2",
      "text": "The output should contain:",
      "page": 8
    },
    {
      "level": "H1",
      "text": "1. Metadata:",
      "page": 8
    },
    {
      "level": "H3",
      "text": "a. Document \nb.  \nc. Refined Text \nd. Page Number Constraints",
      "page": 8
    },
    {
      "level": "H2",
      "text": "\u2022 Must run on CPU only",
      "page": 8
    },
    {
      "level": "H2",
      "text": "\u2022 Model size \u2264 1GB",
      "page": 8
    },
    {
      "level": "H3",
      "text": "\u2022 Processing time \u2264 60 seconds for document collection (3-5 \ndocuments)",
      "page": 8
    },
    {
      "level": "H3",
      "text": "\u2022 No internet access allowed during execution",
      "page": 8
    },
    {
      "level": "H1",
      "text": "Deliverables",
      "page": 9
    },
    {
      "level": "H2",
      "text": "\u2022 approach_explanation.md (300-500 words explaining \nmethodology)",
      "page": 9
    },
    {
      "level": "H2",
      "text": "\u2022 Dockerfile and execution instructions",
      "page": 9
    },
    {
      "level": "H2",
      "text": "Sample input/output for testing",
      "page": 9
    },
    {
      "level": "H1",
      "text": "\u2022",
      "page": 9
    },
    {
      "level": "H1",
      "text": "Scoring Criteria",
      "page": 9
    },
    {
      "level": "H1",
      "text": "Criteria",
      "page": 9
    },
    {
      "level": "H2",
      "text": "Max \nPoints  \nDescription",
      "page": 9
    },
    {
      "level": "H2",
      "text": "Section Relevance   \n60",
      "page": 9
    },
    {
      "level": "H3",
      "text": "Sub-Section Relevance  \n40  \nQuality of granular subsection \nextraction and ranking",
      "page": 9
    },
    {
      "level": "H1",
      "text": "Appendix:",
      "page": 10
    },
    {
      "level": "H1",
      "text": "https://github.com/jhaaj08/Adobe-India-\nHackathon25.git",
      "page": 10
    }
  ]
}

##  Example output - persona_output.json
{
  "persona": "Persona: Blockchain Developer\nJob: Focus on cryptocurrency applications and evaluate security challenges such as attacks, vulnerabilities, and privacy issues in blockchain ecosystems.",
  "results": [
    {
      "document": "My_Research_Paper.pdf",
      "page": 5,
      "heading": "hear about it long before it spreads. The adulthood of \nserviceableness indication projects succeeds marketing by \nrecognizing their obligations to investors, as this has a direct \naffect demand, utility, and serviceableness.  A potential \nresolution to this maybe the Enigma Project, an off-chain \nnetwork to a degree an enlargement to unoriginal blockchain \nfloors.",
      "relevance": 0.352,
      "summary": " Journal of Intelligent and Fuzzy Systems, 42 (2), pp. 1075- 1088."
    }
  ]
}

## Technologies used-
-Python 3.10

-PyMuPDF (fitz)

-SentenceTransformers

-Transformers (t5-small)

-scikit-learn, joblib

-tqdm, json, argparse






