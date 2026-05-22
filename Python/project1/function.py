# 例外処理を行うためのデコレーター関数を定義します
import functools
def handle_errors(error_type=Exception, default=None):
    """error_type: キャッチしたい例外の種類を指定します（デフォルトはExceptionで、すべての例外をキャッチします）
       default: 例外が発生した場合に返す値を指定します（デフォルトはNoneです）"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_type as e:
                print(f"ここが間違っています{func.__name__}: {e}")
                return default
        return wrapper
    return decorator

@handle_errors()
def calculator(number_1, number_2, op):
    # 入力された演算子に応じて、条件分岐（if文）で計算内容を決定します

    number_1 = float(number_1) # 入力された数字を浮動小数点数に変換します
    number_2 = float(number_2) # 同様に、2つ目の数字も変換します
    
    # 足し算の場合
    if op=="+":
         print(f"{number_1} + {number_2} = {number_1 + number_2}")
    # 引き算の場合
    elif op=="-":
        print(f"{number_1} - {number_2} = {number_1 - number_2}")
        # 掛け算の場合
    elif op=="*":
        print(f"{number_1} * {number_2} = {number_1 * number_2}")
        # 割り算の場合
        # 注意: Pythonでは割り算の結果は自動的に小数（float型）になります
    elif op=="/":
        print(f"{number_1} / {number_2} = {number_1 / number_2}")
        # 指定された4つの記号以外の入力があった場合の「例外処理」です
    else:
        print("演算子が正しくありません")

# 例えば、ユーザーが「+」を入力した場合は足し算が実行され、「-」を入力した場合は引き算が実行されます。
def hello(name):
    print(f"Hello, {name}!")

    