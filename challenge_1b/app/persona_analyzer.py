
# from sentence_transformers import SentenceTransformer, util
# from transformers import pipeline

# # Load embedding model for similarity
# embedding_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# # Load summarizer model
# summarizer_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# def summarize_text(text):
#     """
#     Summarize a given section text.
#     Auto-adjust max_length for short sections to avoid warnings.
#     """
#     text = text.strip()
#     word_count = len(text.split())

#     # 🚨 Skip summarizing very short sections
#     if word_count < 15:
#         print(f"⚠️ Skipping summarization for short text ({word_count} words): '{text}'")
#         return text

#     # Dynamically adjust max_length to avoid warning
#     dynamic_max_length = min(50, word_count)
#     dynamic_min_length = min(20, max(5, word_count // 2))

#     try:
#         summary = summarizer_model(
#             text,
#             max_length=dynamic_max_length,
#             min_length=dynamic_min_length,
#             do_sample=False
#         )
#         return summary[0]['summary_text']
#     except Exception as e:
#         print(f"⚠️ Summarization failed: {e}")
#         return text[:200]  # Return first 200 chars as fallback

# def rank_and_summarize(sections, persona_description):
#     """
#     Rank sections by relevance to persona description and summarize them.
#     """
#     persona_embedding = embedding_model.encode(persona_description, convert_to_tensor=True)
#     ranked_sections = []

#     for section in sections:
#         section_embedding = embedding_model.encode(section['text'], convert_to_tensor=True)
#         similarity = util.pytorch_cos_sim(persona_embedding, section_embedding).item()
#         summary = summarize_text(section['text'])

#         ranked_sections.append({
#             "document": section['document'],
#             "page": section['page'],
#             "heading": section['heading'],
#             "relevance": similarity,
#             "summary": summary
#         })

#     ranked_sections.sort(key=lambda x: x['relevance'], reverse=True)
#     return ranked_sections[:10]  # Return top 10











from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# Load embedding model for similarity
embedding_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Load summarizer model
summarizer_model = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    """
    Summarize a section of text. Skip short or noisy content.
    """
    text = text.strip()
    word_count = len(text.split())

    if word_count < 20:
        print(f"⚠️ Skipping summarization for short text ({word_count} words): '{text[:50]}...'")
        return text

    # Adjust summarizer parameters
    max_length = min(50, word_count + 10)
    min_length = min(20, max(5, word_count // 2))

    try:
        summary = summarizer_model(
            text, max_length=max_length, min_length=min_length, do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        print(f"⚠️ Summarization failed: {e}")
        return text[:200]  # Fallback: return first 200 chars

def rank_and_summarize(sections, persona_description):
    """
    Rank sections by relevance to the persona description and summarize them.
    """
    persona_embedding = embedding_model.encode(persona_description, convert_to_tensor=True)
    ranked_sections = []

    for section in sections:
        section_embedding = embedding_model.encode(section['text'], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(persona_embedding, section_embedding).item()

        summary = summarize_text(section['text'])

        ranked_sections.append({
            "document": section['document'],
            "page": section['page'],
            "heading": section['heading'],
            "relevance": round(similarity, 3),
            "summary": summary
        })

    # Sort by relevance (highest first)
    ranked_sections.sort(key=lambda x: x['relevance'], reverse=True)

    # ✅ Always return at least Top 5 sections, even if relevance is low
    if not ranked_sections:
        ranked_sections.append({
            "document": "N/A",
            "page": "N/A",
            "heading": "No relevant sections found.",
            "relevance": 0.0,
            "summary": ""
        })
    return ranked_sections[:5]


