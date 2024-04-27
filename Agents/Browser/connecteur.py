import json

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from dataclasses import dataclass, InitVar, field
from typing import Dict
from pathlib import Path
import os


@dataclass
class Connector:
    profile: InitVar[str] = field(init=True, default="Onche")
    headless: InitVar[bool] = field(init=True, default=False)
    base_url: InitVar[str] = field(init=True, default="https://onche.org/forum/1/blabla-general")

    _driver: Firefox = field(default_factory=Firefox)

    def __post_init__(self, profile: str, headless: bool, base_url: str):
        options = self.__set_option(headless)
        self._driver = Firefox(options=options)
        self._driver.get(base_url)
        self.__load_profile(profile)

    # ----------- Check --------------
    @staticmethod
    def __set_option(headless: bool) -> Options:
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        return options

    def __load_profile(self, profile: str) -> None:
        path_check = Path(f"/home/recitasse/Desktop/programmation/BotNewsOnche/Agents/Browser/profiles/{profile}.json")
        if not path_check.exists():
            FileNotFoundError(f"Le profile {profile} n'existe pas.")

        with open(f"/home/recitasse/Desktop/programmation/BotNewsOnche/Agents/Browser/profiles/{profile}.json", "r", encoding="utf-8") as prof:
            cookies = json.load(prof)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.refresh()
