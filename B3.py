input_line = input("行数を入力してください:")
input_column = input("列数を入力してください:")

input_line = int(input_line)
input_column = int(input_column)

for first_number in range(1, input_line + 1):

    for second_number in range(1, input_column + 1):
        result = str(first_number * second_number)

        print(f"{second_number} × {first_number} = {result.rjust(2)} |", end=" ")
    print()