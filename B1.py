# 1~9までの値を繰り返して変数「first_number」に定義。
for first_number in range(1, 10):
	# 1〜9までの値を繰り返して変数「second_number」に定義。
	for second_number in range(1, 10):
		# 変数「first_number」と変数「second_number」をかけて、毎回最後に空白を入れて出力。
		print(first_number * second_number, end=" ")
	# 改行を出力。
	print()

# ▼変数「first_number」と変数「second_number」の取り出され方がわかる。
for first_number in range(1, 10):
	print(first_number)
	for second_number in range(1, 10):
		print(second_number)
	print()
