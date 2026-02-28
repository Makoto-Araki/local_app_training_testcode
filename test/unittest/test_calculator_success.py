import pytest
import logging
from apps.calculator import divide, divide_custom

# --------------------------------------------------
# 正常系単一パターンテスト
# --------------------------------------------------
def test_divide_success():
    assert divide(4, 2) == 2

# --------------------------------------------------
# 正常系単一パターンテスト(カスタム)
# --------------------------------------------------
def test_divide_custom_success():
    assert divide_custom(4, 2) == 2

# --------------------------------------------------
# 正常系複数パターンテスト
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (4, 2, 2),
        (8, 2, 4),
        (4, 4, 1),
    ],
    ids=[
        'test01',  # テストID
        'test02',  # テストID
        'test03',  # テストID
    ]
)
def test_divide_normal(divide_func, a, b, expected):
    assert divide_func(a, b) == expected

# --------------------------------------------------
# 正常系複数パターンテスト(カスタム)
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (4, 2, 2),
        (8, 2, 4),
        (4, 4, 1),
    ],
    ids=[
        'test04',  # テストID
        'test05',  # テストID
        'test06',  # テストID
    ]
)
def test_divide_custom(divide_custom_func, a, b, expected):
    assert divide_custom_func(a, b) == expected

# --------------------------------------------------
# ログ出力テスト
# --------------------------------------------------
#def test_divide_normal_logs(mock_logger):
#
#    # テスト対象のモジュールをインポート
#    from apps.calculator import divide
#
#    # テスト対象の関数実行（calculator.logger は mock_logger に差し替え済み）
#    divide(4, 2)
#
#    # logger.infoの部分が引数 divide called で１回のみ呼ばれたことを確認
#    mock_logger.info.assert_called_once_with('divide called')

# --------------------------------------------------
# ログ出力テスト - caplog導入
# --------------------------------------------------
def test_divide_normal_logs_caplog(caplog):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide

    # INFOレベル以上のログを捕捉して divide 実行時のログ出力を検証する
    with caplog.at_level(logging.INFO):
        divide(4, 2)

    # divide called のログメッセージが出力されたことを確認する
    assert 'divide called' in caplog.text

# --------------------------------------------------
# ログ出力テスト(カスタム)
# --------------------------------------------------
#def test_divide_custom_logs(mock_logger):
#
#    # テスト対象のモジュールをインポート
#    from apps.calculator import divide_custom
#
#    # テスト対象の関数実行（calculator.logger は mock_logger に差し替え済み）
#    divide_custom(4, 2)
#
#    # logger.infoの部分が引数 divide called で１回のみ呼ばれたことを確認
#    mock_logger.info.assert_called_once_with('divide_custom called')

# --------------------------------------------------
# ログ出力テスト(カスタム) - caplog導入
# --------------------------------------------------
def test_divide_custom_logs_caplog(caplog):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide_custom

    # INFOレベル以上のログを捕捉して divide 実行時のログ出力を検証する
    with caplog.at_level(logging.INFO):
        divide_custom(4, 2)

    # divide_custom called のログメッセージが出力されたことを確認する
    assert 'divide_custom called' in caplog.text
