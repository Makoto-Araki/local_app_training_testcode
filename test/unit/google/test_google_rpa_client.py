from unittest.mock import MagicMock
from apps.google_rpa_client import GoogleRpaClient

# --------------------------------------------------
# open_top_pageメソッドの確認
# --------------------------------------------------
def test_open_top_page_calls_driver_get():

    fake_driver = MagicMock()

    client = GoogleRpaClient(driver=fake_driver)

    client.open_top_page()

    fake_driver.get.assert_called_once_with("https://www.google.com")

# --------------------------------------------------
# get_titleメソッドの確認
# --------------------------------------------------
def test_get_title_returns_driver_title():

    fake_driver = MagicMock()

    fake_driver.title = "Google"

    client = GoogleRpaClient(driver=fake_driver)

    title = client.get_title()

    assert title == "Google"
