import re
from collections import Counter

def extract_keywords(text, top_n=5):
    # Extract words with 4 or more letters
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    # Basic stop words filter to remove common filler words
    stop_words = {'this', 'that', 'with', 'from', 'your', 'have', 'more', 'will', 'text', 'they', 'into'}
    filtered = [w for w in words if w not in stop_words]
    common = Counter(filtered).most_common(top_n)
    return [word for word, freq in common]

def simple_summarize(text):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    if len(sentences) <= 2:
        return text
    # Simple summary combining the introductory and concluding insights
    return f"{sentences[0]} {sentences[-1]}"

# Sample text data for demonstration
sample_text = (
    "Natural language processing is a fascinating field of artificial intelligence. "
    "It enables machines to understand, interpret, and manipulate human text data. "
    "Frequency analysis and regex utilities help in building lightweight keyword extractors. "
    "Maintaining a consistent GitHub portfolio on mobile demonstrates strong technical adaptability."
)

print("=== Keywords & Text Summarizer Demo ===")
print(f"\nOriginal Text:\n{sample_text}\n")

keywords = extract_keywords(sample_text)
print(f"Extracted Keywords: {keywords}")

summary = simple_summarize(sample_text)
print(f"\nSummary:\n{summary}")
