import pytest
#import logging
from apps.calculator import divide, divide_custom

# --------------------------------------------------
# 例外発生テスト
# --------------------------------------------------
#def test_divide_zero(divide_func):
#
#    # このブロック内でZeroDivisionErrorが発生することを期待
#    with pytest.raises(ZeroDivisionError) as exc_info:
#        divide_func(4, 0)
#
#    # 例外メッセージの確認
#    assert "division by zero" in str(exc_info.value)

# --------------------------------------------------
# 例外発生テスト(カスタム)
# --------------------------------------------------
#def test_divide_custom_zero(divide_custom_func):
#
#    # このブロック内でValueErrorが発生することを期待
#    with pytest.raises(ValueError) as exc_info:
#        divide_custom_func(4, 0)
#
#    # 例外メッセージの確認
#    assert "zero divide is forbidden" in str(exc_info.value)

# --------------------------------------------------
# エラーログテスト(カスタム)
# --------------------------------------------------
#def test_divide_custom_zero_logs(mock_logger):
#
#    # テスト対象のモジュールをインポート
#    from apps.calculator import divide_custom
#
#    # このブロック内でZeroDivisionErrorが発生することを期待
#    with pytest.raises(ValueError) as exc_info:
#        divide_custom(4, 0)
#
#    # エラーログの確認
#    mock_logger.error.assert_called_once_with('zero divide is forbidden')

# --------------------------------------------------
# エラーログテスト(カスタム) - caplog導入
# --------------------------------------------------
#def test_divide_custom_zero_logs_caplog(caplog):
#
#    # テスト対象のモジュールをインポート
#    from apps.calculator import divide_custom
#
#    # INFOレベル以上のログを捕捉し、発生する例外は吸収した上で divide_custom 実行時のログ出力を検証する
#    with caplog.at_level(logging.INFO):
#        with pytest.raises(ValueError):
#            divide_custom(4, 0)
#
#    # ログ数を確認する
#    assert len(caplog.records) == 2
#
#    # ログレベルを確認する
#    assert caplog.records[0].levelname == "INFO"
#    assert caplog.records[1].levelname == "ERROR"
#
#    # ログメッセージが出力されたことを確認する
#    assert caplog.records[0].message == 'divide_custom called'
#    assert caplog.records[1].message == 'zero divide is forbidden'

# --------------------------------------------------
# ログ出力テスト - mock使用
# --------------------------------------------------
def test_divide_error_with_mock(mock_logger):

    # 例外発生
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(4, 0, logger=mock_logger)

    # ログ確認
    mock_logger.info.assert_called_once_with('divide called')

# --------------------------------------------------
# ログ出力テスト(カスタム) - mock使用
# --------------------------------------------------
def test_divide_custom_error_with_mock(mock_logger):

    # 例外発生
    with pytest.raises(ValueError, match="zero divide is forbidden"):
        divide_custom(4, 0, logger=mock_logger)

    # ログ確認
    mock_logger.info.assert_called_once_with('divide_custom called')
    mock_logger.error.assert_called_once_with('zero divide is forbidden')
