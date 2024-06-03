from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import random
import xml.etree.ElementTree as ET


nltk.download('vader_lexicon')


def get_sentiment(text: str, nb_split: int = 2) -> list:
    if "." not in text:
        text += "."
    texts = text.split('.')
    sia = SentimentIntensityAnalyzer()

    indexes = []
    neuter = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}

    for i in range(len(texts)):
        if i % nb_split == 0:
            sentiment_nltk = sia.polarity_scores(text)
            indexes.append((texts[i]+". ", sentiment_nltk))
        else:
            indexes.append((texts[i]+'. ', neuter))

    return indexes


def get_random_sticker(type_: str) -> str:
    with open("stickers.xml", 'r', encoding="utf-8") as f:
        r = f.read()
    root = ET.fromstring(r)
    stickers = root.find(type_)
    sitckers_name = [sticker.get('name') for sticker in stickers]
    return random.choice(sitckers_name)


def convert_sentiment_to_stickers(indexs: list) -> str:
    neuter = {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
    global_text = ""
    for i, ind in enumerate(indexs):
        if ind[1] == neuter:
            global_text += f"{ind[0]} {random.choice([':Lire:', ':eril:', ':risijournal:']) if random.randrange(0, 5) == 2 else ''}"
        else:
            if ind[1]['neu'] > 0.95:
                global_text += f"{ind[0]} {get_random_sticker('facts')}"
            if ind[1]['neg'] > 0.1:
                global_text += f"{ind[0]} {get_random_sticker('neg')}"
            if ind[1]['pos'] > 0.1:
                global_text += f"{ind[0]} {get_random_sticker('pos')}"
        if i % 5 == 0:
            global_text += "\n\t"
    return global_text


def add_sentitments(text: str, split_: int = 2) -> str:
    index = get_sentiment(text, nb_split=split_)
    return convert_sentiment_to_stickers(index)

