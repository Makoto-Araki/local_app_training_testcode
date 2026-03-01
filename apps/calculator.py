import logging

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
        - a はint型であること
        - b はint型であること
        - b はゼロでないこと

    正常系:
        a / b の計算結果の整数部分を返却

    異常系:
        - a, b がint型でない制約違反時はValueErrorを送出
        - b がゼロの場合はZeroDivisionErrorを送出(デフォルト動作のため実装なし)
    """

    # ロガー取得
    logger = logger or logging.getLogger(__name__)

    # ログ出力
    logger.info('divide called')

    # 引数がint型かチェック
    if not isinstance(a, int) or not isinstance(b, int):
        logger.error('argument must be integer')
        raise ValueError('argument must be integer')

    # 戻り値を返す
    return int(a / b)

# --------------------------------------------------
# 割り算の関数(カスタム)
# --------------------------------------------------
def divide_custom(a, b, logger=None):
    """
    入力:
        a: int型
        b: int型
        logger: ロガー

    制約:
        - a はint型であること
        - b はint型であること
        - b はゼロでないこと

    正常系:
        a / b の計算結果の整数部分を返却

    異常系:
        - a, b がint型でない制約違反時はValueErrorを送出
        - b がゼロの場合はValueErrorを送出
    """

    # ロガー取得
    logger = logger or logging.getLogger(__name__)

    # ログ出力
    logger.info('divide_custom called')

    # 引数がint型かチェック
    if not isinstance(a, int) or not isinstance(b, int):
        logger.error('argument must be integer')
        raise ValueError('argument must be integer')

    # ゼロ割り算で例外発生
    if b == 0:
        logger.error('zero divide is forbidden')
        raise ValueError('zero divide is forbidden')

    # 戻り値を返す
    return int(a / b)
