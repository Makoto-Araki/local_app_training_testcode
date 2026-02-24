import pytest

# テスト対象のモジュールをインポート
from apps.hello import hello

# テストコード
def test_hello():
    assert hello() == 'Hello'
