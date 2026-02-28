import logging

# モジュール専用のロガー取得
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Hello + 引数 と返す単純な関数
# --------------------------------------------------
def hello(name: str):
    """
    入力:
        name: str型

    制約:
        - nameはstr型であること
        - 空文字は禁止
        - 大文字小文字を問わずhelloは禁止
        - 英字のみ許可(A-Za-z)

    正常系:
        "Hello {name}" を返却

    異常系:
        制約違反時はValueErrorを送出
    """

    # ログ出力
    logger.info('hello called')

    # 数値や空文字やNoneの場合は例外発生
    if not isinstance(name, str) or name == "" or name is None:
        logger.error('argument is invalid')
        raise ValueError('argument is invalid')

    # 引数が大文字小文字を問わずHello場合は例外発生
    if name.lower() == 'hello':
        logger.error('argument is invalid')
        raise ValueError('argument is invalid')

    # 戻り値を返す
    return f'Hello {name}'
