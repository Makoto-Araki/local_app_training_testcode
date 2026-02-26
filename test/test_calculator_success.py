import pytest

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
        'normal-01',  # テストID
        'normal-02',  # テストID
        'normal-03',  # テストID
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
        'normal-04',  # テストID
        'normal-05',  # テストID
        'normal-06',  # テストID
    ]
)
def test_divide_custom(divide_custom_func, a, b, expected):
    assert divide_custom_func(a, b) == expected

# --------------------------------------------------
# ログ出力テスト
# --------------------------------------------------
def test_divide_normal_logs(mock_logger):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide

    # テスト対象の関数実行（calculator.logger は mock_logger に差し替え済み）
    divide(4, 2)

    # logger.infoの部分が引数 divide called で１回のみ呼ばれたことを確認
    mock_logger.info.assert_called_once_with('divide called')

# --------------------------------------------------
# ログ出力テスト(カスタム)
# --------------------------------------------------
def test_divide_custom_logs(mock_logger):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide_custom

    # テスト対象の関数実行（calculator.logger は mock_logger に差し替え済み）
    divide_custom(4, 2)

    # logger.infoの部分が引数 divide called で１回のみ呼ばれたことを確認
    mock_logger.info.assert_called_once_with('divide_custom called')
