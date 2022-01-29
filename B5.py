# 入力された値をint型に変換して配列「numbers」に定義。
# 関数「split()」でスペースで入力された文字を一つ一つ要素として取り出して配列に入れる。
numbers = [int(x) for x in input("データを入力してください(スペース区切り) >").split()]
print(numbers)
# 合計値
# 変数「add」を定義し、初期値を0とする。
add = 0
# 変数「x」に配列「numbers」の値を繰り返し入れていく。
for x in numbers:
    # 変数「add」へ変数「numbers」に入っている値を足していく。（変数addを更新していく）
    add += x
# 全ての繰り返しが終わったところで変数「add」を出力する。
print(f"合計値: {add}")

# 最大値
# 変数「max」を定義し、配列「numbers」のインデント番号[0]をひとまず最大値とする。
max = numbers[0]
# 変数「x」に配列「numbers」の値を繰り返し入れていく。
for x in numbers:
    # もし変数「max」より変数「x」が大きかったら変数「max」を変数「x」の値に置き換える。
    if max < x:
        max = x
# 全ての繰り返しが終わったところで変数「max」を出力する。
print(f"最大値: {max}")

# 最小値
# 変数「min」を定義し、配列「numbers」のインデント番号[0]をひとまず最小値とする。
min = numbers[0]
# 変数「x」に配列「numbers」の値を繰り返し入れていく。
for x in numbers:
    # もし変数「min」より変数「x」が小さかったら変数「min」を変数「x」の値に置き換える。
    if min > x:
        min = x
# 全ての繰り返しが終わったところで変数「min」を出力する。
print(f"最小値: {min}")

# 平均値
# 変数「average」に配列「numbers」の合計÷変数「numbers」の値の個数の結果を定義する。
average = int(add / len(numbers))
# 変数「average」を出力する。
print(f"平均値: {average}")

# 配列の中身を１つずつ取り出す。
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_)
print(*list_)
