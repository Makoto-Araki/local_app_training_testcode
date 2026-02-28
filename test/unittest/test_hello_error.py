import pytest
import logging

# --------------------------------------------------
# 例外発生テスト
# --------------------------------------------------
@pytest.mark.parametrize(
    "invalid_name",
    [
        "hello",
        "Hello",
        "HELLO",
        "HEllo",
        "",
        1,
        0,
        -1,
        None
    ],
    ids=[
        "invalid-name-01",
        "invalid-name-02",
        "invalid-name-03",
        "invalid-name-04",
        "invalid-name-05",
        "invalid-name-06",
        "invalid-name-07",
        "invalid-name-08",
        "invalid-name-09"
    ]
)
def test_hello_error(hello_func, invalid_name):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        hello_func(invalid_name)

    # 例外メッセージの確認
    assert "argument is invalid" in str(exc_info.value)

# --------------------------------------------------
# エラーログテスト - caplog導入
# --------------------------------------------------
def test_hello_error_logs_caplog(caplog):

    # テスト対象のモジュールをインポート
    from apps.hello import hello

    # ERRORレベル以上のログを捕捉し、発生する例外は吸収した上で hello 実行時のログ出力を検証する
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            hello('hello')

    # ログ数を確認する
    assert len(caplog.records) == 1
    # ログレベルを確認する
    assert caplog.records[0].levelname == "ERROR"
    # zero divide is forbidden のログメッセージが出力されたことを確認する
    assert caplog.records[0].message == 'argument is invalid'
