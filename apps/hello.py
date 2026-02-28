import logging

# モジュール専用のロガー取得
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Hello + 引数 と返す単純な関数
# --------------------------------------------------
def hello(name: str):

    # ログ出力
    logger.info('hello called')

    # 引数がHelloまたはhelloの場合は例外発生
    if name == 'Hello' or name == 'hello':
        logger.error('argument is invalid')
        raise ValueError('argument is invalid')

    # 戻り値を返す
    return f'Hello {name}'
