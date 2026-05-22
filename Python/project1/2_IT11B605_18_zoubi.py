from function import calculator


def main():
    while True:
        try:
            num_1 = float(input("数字入れてください: "))
            print(f"最初の数字は{num_1}です")

            num_2 = float(input("数字入れてください: "))
            print(f"2つ目の数字は{num_2}です")

            sign = input("演算子を入れて下さい: ")
            print(f"{num_1} {sign} {num_2}の計算をします")

            calculator(num_1, num_2, sign)
        except ValueError:
            print("数字の入力が正しくありません。もう一度試してください。")
            continue
        except Exception as e:
            print("予期しないエラーが発生しました:", e)
            continue

        again = input("もう一度計算しますか？ (y/n): ")
        if again.strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
