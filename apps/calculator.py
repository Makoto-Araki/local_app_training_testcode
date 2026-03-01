import logging

# モジュール専用のロガー取得
#logger = logging.getLogger(__name__)

# --------------------------------------------------
# 割り算の関数
# --------------------------------------------------
def divide(a, b, logger=None):
    """
    入力:
        a: int型
        b: int型
        logger: ロガー

    制約:
        - aはint型であること
        - bはint型であること

    正常系:
        a / b を返却

    異常系:
        制約違反時はZeroDivisionErrorを送出
    """

    # ロガー取得
    logger = logger or logging.getLogger(__name__)

    # ログ出力
    logger.info('divide called')

    # 戻り値を返す
    return a / b

# --------------------------------------------------
# 割り算の関数(カスタム)
# --------------------------------------------------
def divide_custom(a, b, logger=None):

    # ロガー取得
    logger = logger or logging.getLogger(__name__)

    # ログ出力
    logger.info('divide_custom called')

    # ゼロ割り算で例外発生
    if b == 0:
        logger.error('zero divide is forbidden')
        raise ValueError('zero divide is forbidden')

    # 戻り値を返す
    return a / b
