import pytest

# --------------------------------------------------
# エラーログ出力テスト
# --------------------------------------------------
def test_divide_zero(divide_func):

    # このブロック内でZeroDivisionErrorが発生することを期待
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_func(4, 0)

    # 例外メッセージの確認
    assert "division by zero" in str(exc_info.value)

# --------------------------------------------------
# エラーログ出力テスト(カスタム)
# --------------------------------------------------
def test_divide_custom_zero(divide_custom_func):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        divide_custom_func(4, 0)

    # 例外メッセージの確認
    assert "zero divide is forbidden" in str(exc_info.value)
