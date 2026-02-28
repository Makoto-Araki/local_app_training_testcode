import pytest
from unittest.mock import MagicMock

# 対象モジュールをインポート(logger差し替え用)
import apps.hello as hello_module
import apps.calculator as calculator_module

# テスト対象関数をfixtureとして公開
from apps.hello import hello
from apps.calculator import divide, divide_custom

# --------------------------------------------------
# calculator.loggerをモックに差し替え
# --------------------------------------------------
#@pytest.fixture
#def mock_logger(monkeypatch):
#    mock = MagicMock()
#
#    # logger.infoやlogger.errorの呼び出し有無や回数を検証可能にする
#    monkeypatch.setattr(calculator_module, "logger", mock)
#    return mock

# --------------------------------------------------
# hello.loggerをモックに差し替え
# --------------------------------------------------
@pytest.fixture
def mock_hello_logger(monkeypatch):
    mock = MagicMock()

    # logger.infoやlogger.errorの呼び出し有無や回数を検証可能にする
    monkeypatch.setattr(hello_module, "logger", mock)
    return mock

# --------------------------------------------------
# hello関数を提供する
# --------------------------------------------------
@pytest.fixture
def hello_func():
    return hello

# --------------------------------------------------
# divide関数を提供する
# --------------------------------------------------
@pytest.fixture
def divide_func():
    return divide

# --------------------------------------------------
# divide_custom関数を提供する
# --------------------------------------------------
@pytest.fixture
def divide_custom_func():
    return divide_custom
