from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --------------------------------------------------
# RPA - レイヤー構成 - ゲートウェイ層
# --------------------------------------------------
class GoogleRpaClient:

    GOOGLE_URL = "https://www.google.com"

    def __init__(self, driver=None, headless: bool = True):
        self.driver = driver or self._create_driver(headless)

    def _create_driver(self, headless: bool):
        options = Options()

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        return webdriver.Chrome(options=options)

    def open_top_page(self) -> None:
        self.driver.get(self.GOOGLE_URL)

    def get_title(self) -> str:
        return self.driver.title

    def close(self) -> None:
        self.driver.quit()
