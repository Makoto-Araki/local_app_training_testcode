from selenium import webdriver

# --------------------------------------------------
# RPA - レイヤー構成 - ゲートウェイ層
# --------------------------------------------------
class GoogleRpaClient:

    GOOGLE_URL = "https://www.google.com"

    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome()

    def open_top_page(self) -> None:
        self.driver.get(self.GOOGLE_URL)

    def get_title(self) -> str:
        return self.driver.title

    def close(self) -> None:
        self.driver.quit()
