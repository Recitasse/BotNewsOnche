from pagegetter import extract_text
from processor import preprocess_text
from resume import Resumeur
from gensim.models import Word2Vec
from sentimenter import add_sentitments


def main(url: str, split_: int = 2, ratio: float = 0.6) -> str:
    text = extract_text(url)
    sentences, words = preprocess_text(text)

    summary = Resumeur()
    summary.model = Word2Vec(words, min_count=1, size=100, window=5)
    res = summary.resume(sentences, words, ratio=ratio)
    f_text = add_sentitments(res, split_)
    return f_text


if __name__ == "__main__":
    print(main("https://ria.ru/20231222/pereimenovanie-1917364220.html", ratio=0.3, split_=5))
