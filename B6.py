# 関数「random」を読み込む。
import random

# 変数「input_surface」に入力された値を定義。さらに、int型に変換。
input_surface = int(input("サイコロの面の数は?:"))
# 変数「input_count」に入力された値を定義。さらに、int型に変換。
input_count = int(input("何回振りますか?:"))

# 空の配列「surface_array」を用意
surface_array = []
# 1〜「input_surface」（入力された面の数）までの値を繰り返して変数「result」に定義。
for result in range(1, input_surface + 1):
    # 関数「append()」で配列「surface_array」に変数「result」（サイコロの麺の種類）を追加。
    surface_array.append(result)

# 関数「random()」と「choices()」を使用して、配列「surface_array」から変数「input_count」回、ランダムな値を出力。
# 関数「choice()」は複数の要素をリストで取得。重複OK。
# 関数「sample()」は複数の要素をリストで取得。重複NG。
print(random.choices(surface_array, k=input_count))
