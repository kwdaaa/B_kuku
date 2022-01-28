# 変数「input_line」に入力された値を定義。さらに、int型に変換。
input_line = int(input("行数を入力してください:"))
# 変数「input_column」に入力された値を定義。さらに、int型に変換。
input_column = int(input("列数を入力してください:"))

# 1〜「input_line」（入力された行数）までの値を繰り返して変数「line」に定義。
for line in range(1, input_line + 1):
    # 1〜「input_column」（入力された列数）までの値を繰り返して変数「column」に定義。
    for column in range(1, input_column + 1):
        # 変数「line」と変数「column」ををかけた値を、変数「result」に定義。さらに、str型に変換。
        result = str(line * column)
        # 関数「rjust()」を使って、右寄せにする。()の中の数字は何文字かを指定する。毎回最後に空白を入れて出力。
        print(f"{column} × {line} = {result.rjust(2)} |", end=" ")
    # 改行を出力。
    print()
