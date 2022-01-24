# input_number = input("ここ").split
# print(input_number)
#
# surface_array = []
# surface_array.append(input_number)
# print(surface_array)

# 入力された値をintがたに変換して配列に入れる。
numbers = [int(x) for x in input("データを入力してください(スペース区切り) >").split()]

# 合計値
add = 0
for i in numbers:
    add += i
print(f"合計値: {add}")

# 最大値
max = numbers[0]
for i in numbers:
    if max < i:
        max = i
print(f"最大値: {max}")

# 最小値
min = numbers[0]
for i in numbers:
    if min > i:
        min = i
print(f"最小値: {min}")

# 平均値
average = int(add / len(numbers))
print(f"平均値: {average}")
