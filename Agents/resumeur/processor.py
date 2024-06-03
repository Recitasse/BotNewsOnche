import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


nltk.download("punkt")
nltk.download("stopwords")


def preprocess_text(text: str) -> tuple:
    sentences = sent_tokenize(text, language="french")
    stop_words = set(stopwords.words("french"))

    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    words = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in words]

    return sentences, words
