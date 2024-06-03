from gensim.summarization import summarize
from gensim.models import Word2Vec

from dataclasses import dataclass, field, InitVar
from typing import ClassVar


@dataclass(init=False)
class Resumeur:
    model_: Word2Vec = field(default=Word2Vec, init=False)

    def resume(self, sentences, words, ratio: float) -> str:
        sentence_vectors = []
        for sentence in words:
            if len(sentence) != 0:
                sentence_vec = sum([self.model_.wv[word] for word in sentence]) / len(sentence)
                sentence_vectors.append(sentence_vec)

        summary = summarize(" ".join(sentences), ratio=ratio, word_count=None, split=False)

        return summary

    @property
    def model(self) -> Word2Vec:
        return self.model_

    @model.setter
    def model(self, inputs: Word2Vec):
        self.model_ = inputs

