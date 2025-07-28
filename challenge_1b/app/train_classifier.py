import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

# === 1️⃣ Dummy Training Data ===
texts = [
    "Introduction", "Conclusion", "Summary", "Overview",
    "What is Artificial Intelligence?", "Deep Learning Techniques",
    "Chapter 1: Getting Started", "Acknowledgments",
    "Machine Learning Basics", "History of AI",
    "This is a normal paragraph with multiple sentences and detailed explanation.",
    "Here is another block of text that is clearly not a heading and just regular content."
]

labels = [
    "H1", "H1", "H1", "H1",  # Big headings
    "H2", "H2", "H2", "H2",  # Sub-headings
    "H3", "H3",              # Minor headings
    "Normal", "Normal"       # Regular paragraphs
]

# === 2️⃣ Build ML Pipeline ===
# Vectorizer: converts text to TF-IDF features
# Classifier: simple logistic regression
model = make_pipeline(
    TfidfVectorizer(),
    LogisticRegression(max_iter=500)
)

# Train the model
model.fit(texts, labels)

# === 3️⃣ Save the Model ===
joblib.dump(model, "classifier.pkl")
print("✅ classifier.pkl saved successfully!")
