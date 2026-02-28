import pytest

# --------------------------------------------------
# エラーログ出力テスト
# --------------------------------------------------
def test_hello_invalid(hello_func):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func('Hello')

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)
