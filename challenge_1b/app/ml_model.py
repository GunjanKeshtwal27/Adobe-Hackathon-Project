# import joblib
# from sentence_transformers import SentenceTransformer

# # Load lightweight embedding model (under 100MB)
# embedding_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# # Load pre-trained classifier (under 1MB)
# classifier = joblib.load("app/models/classifier.pkl")

# def predict_heading_level(text):
#     """
#     Given a text block, predict whether it is H1, H2, H3, or normal.
#     """
#     embedding = embedding_model.encode([text])
#     predicted_label = classifier.predict(embedding)[0]
#     return predicted_label






# def predict_heading_level(text):
#     """
#     Dummy predictor: uses simple heuristics.
#     """
#     if len(text.split()) < 5:  # Short text, probably a heading
#         return "H1"
#     elif len(text.split()) < 10:
#         return "H2"
#     else:
#         return "Normal"













# app/ml_model.py

def predict_heading_level(text):
    """
    Dummy function: Predict heading level without ML.
    """
    # Simple heuristic: shorter lines are probably headings
    word_count = len(text.split())

    if word_count < 3:
        return "H1"
    elif word_count < 7:
        return "H2"
    elif word_count < 12:
        return "H3"
    else:
        return "Normal"

