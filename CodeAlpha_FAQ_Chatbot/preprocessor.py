import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
def preprocess(text):
    text=text.lower()
    # Remove punctuation using regex
    text=re.sub(r"[^a-z\s]","",text)
    # Tokenize the text
    tokens=word_tokenize(text)
    # Remove stop words
    stop_words=set(stopwords.words("english"))
    tokens=[words for words in tokens if words not in stop_words]
    # Stemming
    stemmer=PorterStemmer()
    tokens=[stemmer.stem(word) for word in tokens]
    return " ".join(tokens)