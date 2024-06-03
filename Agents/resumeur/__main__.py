from pagegetter import extract_text
from processor import preprocess_text
from resume import Resumeur
from gensim.models import Word2Vec


def main(url: str) -> str:
    text = extract_text(url)
    sentences, words = preprocess_text(text)

    summary = Resumeur()
    summary.model = Word2Vec(words, min_count=1, size=10, window=5)
    res = summary.resume(sentences, words, ratio=0.1)
    return res


if __name__ == "__main__":
    print(main("https://fr.wikipedia.org/wiki/Intelligence_artificielle"))
