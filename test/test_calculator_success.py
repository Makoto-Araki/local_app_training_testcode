import pytest

# 正常系複数パターンテスト
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

# 正常系複数パターンテスト
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
def test_divide_normal(divide_custom_func, a, b, expected):
    assert divide_custom_func(a, b) == expected

# ログ出力テスト
def test_divide_logs(mock_logger):
    from apps.calculator import divide

    divide(4, 2)

    mock_logger.info.assert_called_once_with('divide called')
