input_line = input("行数を入力してください:")
input_column = input("列数を入力してください:")

input_line = int(input_line)
input_column = int(input_column)

for first_number in range(1, input_line + 1):

    for second_number in range(1, input_column + 1):
        print(first_number * second_number, end=" ")
    print()
