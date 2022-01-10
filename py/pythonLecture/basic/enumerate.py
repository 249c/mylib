fruits = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruits:
#     print(fruit)

# enumerateがどのような値を返すのか確認
# Tuple型
for x in enumerate(fruits):
    print(x)

# idxと要素をそれぞれ出力
for idx, fruit in enumerate(fruits):
    print(idx)
    print(fruit)



