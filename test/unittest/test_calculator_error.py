import pytest
import logging

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
def test_divide_custom_zero_logs_caplog(caplog):

    # テスト対象のモジュールをインポート
    from apps.calculator import divide_custom

    # ERRORレベル以上のログを捕捉し、発生する例外は吸収した上で divide_custom 実行時のログ出力を検証する
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            divide_custom(4, 0)

    # ログ数を確認する
    assert len(caplog.records) == 1
    # ログレベルを確認する
    assert caplog.records[0].levelname == "ERROR"
    # zero divide is forbidden のログメッセージが出力されたことを確認する
    assert caplog.records[0].message == 'zero divide is forbidden'
