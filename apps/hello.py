import logging
import re

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
        - 英字(A-Za-z)のみ許可
        - 3文字以上
        - 20文字以下
        - 先頭は大文字

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

    # 英字(A-Za-z)のみ許可、3文字以上、20文字以下、先頭は大文字を満たさない場合は例外発生
    pattern = r'^[A-Z][A-Za-z]{2,19}$'
    if re.fullmatch(pattern, name) is None:
        logger.error('argument is invalid')
        raise ValueError('argument is invalid')

    # 引数が大文字小文字を問わずHello場合は例外発生
    if name.lower() == 'hello':
        logger.error('argument is invalid')
        raise ValueError('argument is invalid')

    # 戻り値を返す
    return f'Hello {name}'
