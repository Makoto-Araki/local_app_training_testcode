import pytest
from unittest.mock import MagicMock
from apps.calculator import divide, divide_custom
import apps.calculator as calculator

@pytest.fixture
def mock_logger(monkeypatch):
    mock = MagicMock()

    # calculator.loggerをmockに差し替え
    monkeypatch.setattr(calculator, "logger", mock)

    # mockを返す
    return mock

@pytest.fixture
def divide_func():
    return divide

@pytest.fixture
def divide_custom_func():
    return divide_custom
