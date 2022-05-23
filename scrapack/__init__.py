from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from scrapack.function import Selectors


class ScrapBase(Selectors):
    def __init__(self) -> None:
        self.chrome_profile_settings()
        self.args_from_environment()
        super().__init__()

    def chrome_profile_settings(self):
        chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

    def quit(self):
        self.driver.quit()

    def args_from_environment(self):

        self.username = os.environ.get("USERNAME")
        self.password = os.environ.get("PASSWORD")
