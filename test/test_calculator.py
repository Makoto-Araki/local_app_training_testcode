import pytest

# テスト対象のモジュールをインポート
from apps.calculator import divide, divide_custom

# 正常系テスト
def test_divide_success():
    assert divide(4, 2) == 2

# 正常系テスト
def test_divide_custom_success():
    assert divide_custom(4, 2) == 2

# ゼロ除算例外テスト
def test_divide_zero():

    # このブロック内でZeroDivisionErrorが発生することを期待
    with pytest.raises(ZeroDivisionError) as exec_info:
        divide(4, 0) # 例外発生ならテスト成功

    # 例外メッセージの確認
    assert 'division by zero' in str(exec_info.value)

# ゼロ除算例外テスト(独自raise)
def test_divide_zero_custom():

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exec_info:
        divide_custom(4, 0) # 例外発生ならテスト成功

    # 例外メッセージの確認
    assert 'zero divide is forbidden' in str(exec_info.value)

# 複数の正常系テスト
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
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected
