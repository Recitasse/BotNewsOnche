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
    headless: InitVar[bool] = field(init=True, default=False)

    _driver: Firefox = field(default_factory=Firefox)
    _profile: Options = field(default_factory=Options)

    def __post_init__(self, headless: bool):
        self._options = self.__set_option(headless)
        self._driver = Firefox(options=self._options)

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

    def load_profile(self, profile: str) -> None:
        path_check = Path(f"/home/recitasse/Desktop/programmation/BotNewsOnche/Agents/Browser/profiles/{profile}.json")
        if not path_check.exists():
            FileNotFoundError(f"Le profile {profile} n'existe pas.")

        with open(f"/home/recitasse/Desktop/programmation/BotNewsOnche/Agents/Browser/profiles/{profile}.json", "r", encoding="utf-8") as prof:
            cookies = json.load(prof)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
        self._driver.refresh()
