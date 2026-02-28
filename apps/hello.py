import logging

# モジュール専用のロガー取得
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Helloと返す単純な関数
# --------------------------------------------------
def hello():

    # ログ出力
    logger.info('hello called')

    # 戻り値を返す
    return 'Hello'
