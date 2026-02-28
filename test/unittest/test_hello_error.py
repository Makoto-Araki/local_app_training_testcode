import pytest

# --------------------------------------------------
# 例外発生テスト
# --------------------------------------------------
@pytest.mark.parametrize(
    "invalid_name",
    [
        "hello",
        "Hello",
        "HELLO",
        "HEllo"
    ],
    ids=[
        "invalid-name-01",
        "invalid-name-02",
        "invalid-name-03",
        "invalid-name-04"
    ]
)
def test_hello_error(hello_func, invalid_name):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func(invalid_name)

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)

# --------------------------------------------------
# エラーログ出力テスト
# --------------------------------------------------
@pytest.mark.parametrize(
    "invalid_name",
    [
        "hello",
        "Hello",
        "HELLO",
        "HEllo"
    ],
    ids=[
        "invalid-name-01",
        "invalid-name-02",
        "invalid-name-03",
        "invalid-name-04"
    ]
)
def test_hello_invalid(hello_func, invalid_name):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func(invalid_name)

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)
