import requests
from bs4 import BeautifulSoup
from translate import Translator


def extract_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    trans = Translator(to_lang='fr')

    return trans.translate(text)
