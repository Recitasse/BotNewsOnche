import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from langdetect import detect


def translate(text: str) -> str:
    slices = []
    glb = ""
    for i in range(0, len(text), 4500):
        slices.append(text[i:i + 4500])

    for text in slices:
        jm = GoogleTranslator(source=detect(text), target='fr').translate(text+".")
        glb += jm
    return glb


def extract_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    if detect(text) == "fr":
        return text
    return translate(text)
