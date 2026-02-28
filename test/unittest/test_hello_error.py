import pytest

# --------------------------------------------------
# 例外発生テスト
# --------------------------------------------------
def test_divide_error(divide_func):

    # テスト対象のモジュールをインポート
    from apps.hello import hello

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello('Hello')

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)

# --------------------------------------------------
# エラーログ出力テスト
# --------------------------------------------------
def test_hello_invalid(hello_func):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func('Hello')

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)

# --------------------------------------------------
# エラーログ出力テスト
# --------------------------------------------------
def test_hello_invalid_lowercase(hello_func):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func('hello')

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)
