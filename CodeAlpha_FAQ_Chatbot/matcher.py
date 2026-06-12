from sklearn.feature_extraction.text import TfidfVectorizer
from faq_data import faqs
from preprocessor import preprocess
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
        
class FAQMatcher:
    def __init__(self):
        self.faqs = faqs
        # 1. Preprocess every FAQ question
        self.processed_questions = [preprocess(f["question"]) for f in faqs]
        # 2. Fit TF-IDF on those cleaned questions
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)
    def get_answer(self, user_input):
        cleaned = preprocess(user_input)
        # transform() reuses the vocabulary learned from FAQs
        user_vector = self.vectorizer.transform([cleaned])
        scores = cosine_similarity(user_vector, self.tfidf_matrix).flatten()
        best_idx = int(np.argmax(scores))
        best_score = float(scores[best_idx])
        if best_score < 0.2:   # tune this threshold
            return "I'm not sure about that. Could you rephrase?"
        return self.faqs[best_idx]["answer"]