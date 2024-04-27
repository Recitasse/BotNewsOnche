from Agents.Browser.connecteur import Connector
from selenium.webdriver.common.by import By

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Onche(Connector):
    base_url: ClassVar[str] = field(default="https://onche.org/forum/1/blabla-general")

    def go_to_topic(self, url: int) -> None:
        """
        Permet de se rendre à la page si l'on possède l'id du topic
        :param url: id du topic
        :return: None
        """
        url = f"https://onche.org/topic/{url}"
        self._driver.get(url)

    def post_message(self, url: int | str, message: str) -> None:
        """
        Post un message dans le topic donné
        :param url: id topic
        :param message: message formalisé
        :return:
        """
        self._check_current_url(url)
        text_box = self._driver.find_element(By.CLASS_NAME, 'textarea')
        text_box.send_keys(message)
        button = self._driver.find_element(By.CLASS_NAME, 'button')
        button.click()

    def _check_current_url(self, url: str | int) -> None:
        """
        Evite de recharger la page si l'on s'y trouve déjà
        :param url: id du topic ou l'url complète
        :return: None
        """
        base_url = self._driver.current_url
        if not str(url) in base_url:
            self._driver.get(self.__url_format(str(url)))

    @staticmethod
    def __url_format(url: int | str) -> str:
        return f"https://onche.org/topic/{str(url)}"
