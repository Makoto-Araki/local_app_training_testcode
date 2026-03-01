import pytest
import logging
from unittest.mock import MagicMock
from apps.hello import hello

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
        None,
        "tanaka1",  # 数字が混入
        "1tanaka",  # 数字が混入
        "ta",       # 3文字未満
        "TanakaTanakaTanakaTanaka",  # 20文字より多い
        "tanaka"    # 先頭が大文字でない
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
        "invalid-name-09",
        "invalid-name-10",
        "invalid-name-11",
        "invalid-name-12",
        "invalid-name-13",
        "invalid-name-14"
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
#def test_hello_error_logs_caplog(caplog):
#
#    # テスト対象のモジュールをインポート
#    from apps.hello import hello
#
#    # ERRORレベル以上のログを捕捉し、発生する例外は吸収した上で hello 実行時のログ出力を検証する
#    with caplog.at_level(logging.ERROR):
#        with pytest.raises(ValueError):
#            hello('hello')
#
#    # ログ数を確認する
#    assert len(caplog.records) == 1
#    # ログレベルを確認する
#    assert caplog.records[0].levelname == "ERROR"
#    # zero divide is forbidden のログメッセージが出力されたことを確認する
#    assert caplog.records[0].message == 'argument is invalid'

# --------------------------------------------------
# 例外発生とログ検証を同時テスト
# --------------------------------------------------
def test_hello_error_logs_caplog(caplog):

    # テスト対象のモジュールをインポート
    from apps.hello import hello

    # INFOレベル以上のログを捕捉し、発生する例外は吸収した上で hello 実行時のログ出力を検証する
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError) as exc_info:
            hello('hello')

    # --------------------------------------------------
    # 例外発生
    # --------------------------------------------------

    assert str(exc_info.value) == "argument is invalid"

    # --------------------------------------------------
    # ログ検証
    # --------------------------------------------------

    # ログ数を確認する
    assert len(caplog.records) == 2

    # ログレベルを確認する
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[1].levelname == "ERROR"

    # zero divide is forbidden のログメッセージが出力されたことを確認する
    assert caplog.records[0].message == 'hello called'
    assert caplog.records[1].message == 'argument is invalid'

# --------------------------------------------------
# エラーログテスト - mock使用
# --------------------------------------------------
def test_hello_error_with_mock():
    mock_logger = MagicMock()

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError):
        hello('hello', logger=mock_logger)

    # テスト確認
    mock_logger.info.assert_called_once_with('hello called')
    mock_logger.error.assert_called_once_with('argument is invalid')
