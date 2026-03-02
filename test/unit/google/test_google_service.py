from unittest.mock import MagicMock
from apps.google_service import GoogleService

# --------------------------------------------------
# executeメソッドの確認
# --------------------------------------------------
def test_execute_returns_title():

    mock_rpa = MagicMock()
    mock_rpa.get_title.return_value = "Google"

    service = GoogleService(mock_rpa)

    result = service.execute()

    assert result == "Google"
    mock_rpa.open_top_page.assert_called_once()
    mock_rpa.get_title.assert_called_once()