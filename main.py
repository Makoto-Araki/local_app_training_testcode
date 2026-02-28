import logging
from apps.hello import hello
from apps.calculator import divide, divide_custom

# --------------------------------------------------
# メイン関数
# --------------------------------------------------
def main():
    greeting = hello()
    print(f'挨拶：{greeting}')

    answer = divide(4, 2)
    print(f'回答：{answer}')

# --------------------------------------------------
# コマンド python main.py で main.py を直接実行時にコード実行
# --------------------------------------------------
if __name__ == "__main__":
    # loggigの初期化設定
    logging.basicConfig(
        # ログレベル設定
        level=logging.INFO,
        # ログフォーマット
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    main()