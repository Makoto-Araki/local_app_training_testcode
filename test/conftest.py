import pytest
from unittest.mock import MagicMock
import apps.hello as hello_module
from apps.hello import hello
import apps.calculator as calculator_module
from apps.calculator import divide, divide_custom
import apps.calculator as calculator

@pytest.fixture
def mock_logger(monkeypatch):
    mock = MagicMock()

    # calculator.loggerをmockに差し替え
    monkeypatch.setattr(calculator_module, "logger", mock)
    return mock

@pytest.fixture
def mock_hello_logger(monkeypatch):
    mock = MagicMock()

    # hello.loggerをmockに差し替え
    monkeypatch.setattr(hello_module, "logger", mock)
    return mock

@pytest.fixture
def hello_func():
    return hello

@pytest.fixture
def divide_func():
    return divide

@pytest.fixture
def divide_custom_func():
    return divide_custom
