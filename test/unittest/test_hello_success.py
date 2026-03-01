import pytest
import logging
from unittest.mock import MagicMock
from apps.hello import hello

# --------------------------------------------------
# 正常系テスト
# --------------------------------------------------
#def test_hello(hello_func):
#
#    # 戻り値を確認
#    assert hello_func('Tanaka') == 'Hello Tanaka'

# --------------------------------------------------
# ログ出力テスト
# --------------------------------------------------
#def test_hello_logs(mock_hello_logger):
#
#    # テスト対象のモジュールをインポート
#    from apps.hello import hello
#
#    # テスト対象の関数実行（hello.logger は mock_hello_logger に差し替え済み）
#    hello('Tanaka')
#
#    # logger.infoの部分が引数 hello called で１回のみ呼ばれたことを確認
#    mock_hello_logger.info.assert_called_once_with('hello called')

# --------------------------------------------------
# ログ出力テスト - caplog導入
# --------------------------------------------------
#def test_hello_logs(caplog):
#
#    # テスト対象のモジュールをインポート
#    from apps.hello import hello
#
#    # INFOレベル以上のログを捕捉して divide 実行時のログ出力を検証する
#    with caplog.at_level(logging.INFO):
#        hello('Tanaka')
#
#    # hello called のログメッセージが出力されたことを確認する
#    assert 'hello called' in caplog.text

# --------------------------------------------------
# ログ出力テスト - mock使用
# --------------------------------------------------
def test_hello_success_with_mock():
    mock_logger = MagicMock()

    # ロガーを外部から注入
    result = hello('Tanaka', logger=mock_logger)

    # テスト確認
    assert result == "Hello Tanaka"
    mock_logger.info.assert_called_once_with('hello called')
    mock_logger.error.assert_not_called()
