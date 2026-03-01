import pytest
from apps.calculator import divide, divide_custom

# --------------------------------------------------
# 振る舞いテスト - 正常系
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (4, 2, 2),
        (8, 2, 4),
        (4, 4, 1),
        (4, 1, 4),
        (-4, 2, -2),
        (-8, 2, -4),
        (-4, 4, -1),
        (-4, 1, -4),
        (4, -2, -2),
        (8, -2, -4),
        (4, -4, -1),
        (4, -1, -4)
    ],
    ids=[
        'valid-argument-01',
        'valid-argument-02',
        'valid-argument-03',
        'valid-argument-04',
        'valid-argument-05',
        'valid-argument-06',
        'valid-argument-07',
        'valid-argument-08',
        'valid-argument-09',
        'valid-argument-10',
        'valid-argument-11',
        'valid-argument-12'
    ]
)
def test_divide_success_logging(a, b, expected, mock_logger):

    # 関数実行
    try:
        divide(a, b, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide called')
    mock_logger.error.error.assert_not_called()

# --------------------------------------------------
# 振る舞いテスト - 異常系
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b',
    [
        ("4", 2), # a がint型でない
        (8, "2"), # b がint型でない
    ],
    ids=[
        'invalid-argument-01',
        'invalid-argument-02'
    ]
)
def test_divide_error_logging_argument_not_integer(a, b, mock_logger):

    # 関数実行
    try:
        divide(a, b, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide called')
    mock_logger.error.assert_called_once_with('argument must be integer')

# --------------------------------------------------
# 振る舞いテスト - 異常系
# --------------------------------------------------
def test_divide_error_logging_argument_is_zero(mock_logger):

    # 関数実行
    try:
        divide(4, 0, mock_logger)
    except ZeroDivisionError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide called')

# --------------------------------------------------
# 振る舞いテスト(カスタム) - 正常系
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (4, 2, 2),
        (8, 2, 4),
        (4, 4, 1),
        (4, 1, 4),
        (-4, 2, -2),
        (-8, 2, -4),
        (-4, 4, -1),
        (-4, 1, -4),
        (4, -2, -2),
        (8, -2, -4),
        (4, -4, -1),
        (4, -1, -4)
    ],
    ids=[
        'valid-argument-01',
        'valid-argument-02',
        'valid-argument-03',
        'valid-argument-04',
        'valid-argument-05',
        'valid-argument-06',
        'valid-argument-07',
        'valid-argument-08',
        'valid-argument-09',
        'valid-argument-10',
        'valid-argument-11',
        'valid-argument-12',
    ]
)
def test_divide_custom_success_logging(a, b, expected, mock_logger):

    # 関数実行
    try:
        divide_custom(a, b, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide_custom called')
    mock_logger.error.error.assert_not_called()

# --------------------------------------------------
# 振る舞いテスト(カスタム) - 異常系
# --------------------------------------------------
@pytest.mark.parametrize(
    'a, b',
    [
        ("4", 2), # a がint型でない
        (8, "2"), # b がint型でない
    ],
    ids=[
        'invalid-argument-01',
        'invalid-argument-02'
    ]
)
def test_divide_custom_error_logging_argument_not_integer(a, b, mock_logger):

    # 関数実行
    try:
        divide_custom(a, b, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide_custom called')
    mock_logger.error.assert_called_once_with('argument must be integer')

# --------------------------------------------------
# 振る舞いテスト(カスタム) - 異常系
# --------------------------------------------------
def test_divide_custom_error_logging_argument_is_zero(mock_logger):

    # 関数実行
    try:
        divide_custom(4, 0, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('divide_custom called')
    mock_logger.error.assert_called_once_with('zero divide is forbidden')
