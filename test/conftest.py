import pytest
from unittest.mock import MagicMock

# --------------------------------------------------
# ロガー差し替えのための共通モック
# --------------------------------------------------
@pytest.fixture
def mock_logger():
    return MagicMock()
