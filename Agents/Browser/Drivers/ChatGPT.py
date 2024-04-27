from Agents.Browser.connecteur import Connector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dataclasses import dataclass, field, InitVar
from typing import ClassVar


@dataclass
class GPT(Connector):
    base_url: ClassVar[str] = field(default="https://chat.openai.com/g/g-Tu3DzxTMe-resume")

    def resume_text(self, text: str):
        wait = WebDriverWait(self._driver, 60)
        text_box = wait.until(EC.presence_of_element_located((By.ID, 'prompt-textarea')))
        text_box.send_keys(text)
        wait = WebDriverWait(self._driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'text-white')))
        button.click()

    def connexion(self, profile: str):
        self._driver.get(self.base_url)
        self.load_profile(profile)


if __name__ == "__main__":
    g = GPT(False)
    g.connexion("gpt")
    g.resume_text("""Les Jeux Olympiques de Paris 2024 seront le plus grand événement jamais organisé en France. Ils se tiendront du 26 juillet au 11 août 2024, durant 16 jours hors du temps pendant lesquels Paris 2024 sera le cœur du monde. Les Jeux, c’est du sport, mais tellement plus encore… Une combinaison de rendez-vous culturels, de programmation artistique, et de performances diverses qui créent une expérience unique en son genre. Les Jeux, c’est un festival populaire et multiculturel qui s’adresse au monde entier. C’est une aventure qui va embarquer la France entière pour une expérience inédite.

Les Jeux sont un rendez-vous unique pour lequel Paris 2024 travaille depuis la phase de candidature. En décrochant l’organisation des Jeux Olympiques et Paralympiques le 13 septembre 2017, Paris 2024 s’est lancé dans l’aventure avec une ambition : proposer des Jeux révolutionnaires.
Les Jeux Olympiques en quelques chiffres

    Plusieurs milliards de téléspectateurs
    350 000 heures de diffusion TV (Rio 2016)
    9,7 millions de spectateurs
    35 sites de compétition
    10 500 athlètes
    6 000 journalistes accrédités
    45 000 volontaires dédiés
    + 600 000 repas servis par jour au Village des athlètes

Les Jeux Olympiques de Paris 2024

    XXXIIIe Olympiade
    26 juillet au 11 août 2024
    19 jours de compétition (les tournois de handball, football et rugby débuteront le 24 juillet)
    Athlètes de plus de 200 Comités Nationaux Olympiques et l'équipe olympique des réfugiés
    32 sports (y compris 4 sports additionnels)
    329 épreuves
    754 sessions (compétitions et cérémonies)
    10 500 athlètes

Le calendrier des sports de Paris 2024""")