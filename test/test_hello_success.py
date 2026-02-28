import pytest

# --------------------------------------------------
# 正常系テスト
# --------------------------------------------------
def test_hello(hello_func):
    assert hello_func() == 'Hello'

# --------------------------------------------------
# ログ出力テスト
# --------------------------------------------------
def test_hello_logs(mock_hello_logger):

    # テスト対象のモジュールをインポート
    from apps.hello import hello

    # テスト対象の関数実行（hello.logger は mock_hello_logger に差し替え済み）
    hello()

    # logger.infoの部分が引数 hello called で１回のみ呼ばれたことを確認
    mock_hello_logger.info.assert_called_once_with('hello called')
