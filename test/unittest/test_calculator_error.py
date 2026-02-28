import pytest

# --------------------------------------------------
# 例外発生テスト
# --------------------------------------------------
def test_divide_zero(divide_func):

    # このブロック内でZeroDivisionErrorが発生することを期待
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_func(4, 0)

    # 例外メッセージの確認
    assert "division by zero" in str(exc_info.value)

# --------------------------------------------------
# 例外発生テスト(カスタム)
# --------------------------------------------------
def test_divide_custom_zero(divide_custom_func):

    # このブロック内でValueErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        divide_custom_func(4, 0)

    # 例外メッセージの確認
    assert "zero divide is forbidden" in str(exc_info.value)

# --------------------------------------------------
# エラーログテスト(カスタム)
# --------------------------------------------------
def test_divide_custom_zero_logs(mock_logger):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide_custom

    # このブロック内でZeroDivisionErrorが発生することを期待
    with pytest.raises(ValueError) as exc_info:
        divide_custom(4, 0)

    # エラーログの確認
    mock_logger.error.assert_called_once_with('zero divide is forbidden')
