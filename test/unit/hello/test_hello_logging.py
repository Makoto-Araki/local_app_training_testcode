import pytest
from apps.hello import hello

# --------------------------------------------------
# ロギングテスト - 正常系
# --------------------------------------------------
def test_hello_success_logging(mock_logger):

    # 関数実行
    hello('Tanaka', logger=mock_logger)

    # ロギング確認
    mock_logger.info.assert_called_once_with('hello called')
    mock_logger.error.assert_not_called()

# --------------------------------------------------
# ロギングテスト - 異常系
# --------------------------------------------------
@pytest.mark.parametrize(
    "invalid_argument",
    [
        "hello",
        "Hello",
        "HELLO",
        "HEllo",
        "",
        1,
        0,
        -1,
        None,
        "tanaka1",  # 数字が混入
        "1tanaka",  # 数字が混入
        "ta",       # 3文字未満
        "TanakaTanakaTanakaTanaka",  # 20文字より多い
        "tanaka"    # 先頭が大文字でない
    ],
    ids=[
        "invalid-argument-01",
        "invalid-argument-02",
        "invalid-argument-03",
        "invalid-argument-04",
        "invalid-argument-05",
        "invalid-argument-06",
        "invalid-argument-07",
        "invalid-argument-08",
        "invalid-argument-09",
        "invalid-argument-10",
        "invalid-argument-11",
        "invalid-argument-12",
        "invalid-argument-13",
        "invalid-argument-14"
    ]
)
def test_hello_error_logging(invalid_argument, mock_logger):

    # 関数実行
    try:
        hello(invalid_argument, mock_logger)
    except ValueError:
        pass

    # ロギング確認
    mock_logger.info.assert_called_once_with('hello called')
    mock_logger.error.assert_called_once_with('argument is invalid')
