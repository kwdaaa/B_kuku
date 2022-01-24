import random

input_surface = input("サイコロの面の数は?:")
input_count = input("何回振りますか?:")

surface = int(input_surface)
count = int(input_count)

# 空の配列「surface_array」を用意
surface_array = []
# サイコロの面の種類を抽出
for result in range(1, surface + 1):
    # 結果を「surface_array」配列に追加
    surface_array.append(result)

# 配列「surface_array」から「count」回、ランダムな値を抽出（重複OK）
print(random.choices(surface_array, k=count))
