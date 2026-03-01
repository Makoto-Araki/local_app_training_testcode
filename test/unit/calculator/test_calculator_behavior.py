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
def test_divide_success_behavior(a, b, expected):

    # 関数実行と結果確認
    assert expected == divide(a, b)

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
def test_divide_error_behavior_argument_not_integer(a, b):

    # 例外発生を補足
    with pytest.raises(ValueError, match="argument must be integer"):
        divide(a, b)

# --------------------------------------------------
# 振る舞いテスト - 異常系
# --------------------------------------------------
def test_divide_error_behavior_argument_is_zero():

    # 例外発生を補足
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(4, 0)

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
def test_divide_custom_success_behavior(a, b, expected):

    # 関数実行と結果確認
    assert expected == divide_custom(a, b)

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
def test_divide_custom_error_behavior_argument_not_integer(a, b):

    # 例外発生を補足
    with pytest.raises(ValueError, match="argument must be integer"):
        divide_custom(a, b)

# --------------------------------------------------
# 振る舞いテスト(カスタム) - 異常系
# --------------------------------------------------
def test_divide_custom_error_behavior_argument_is_zero():

    # 例外発生を補足
    with pytest.raises(ValueError, match="zero divide is forbidden"):
        divide_custom(4, 0)
