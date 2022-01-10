# dictionary: キーと値の組み合わせを複数保持するデータ型
# indexではなく自分でkeyを設定することができる
# { key1: value1, key2: value2, ...}

fruits_colors = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
print(fruits_colors)
print(fruits_colors['apple'])  # 存在しないkeyの場合error

# 新しい要素の追加
fruits_colors['peach'] = 'pink'  # あれば更新, なければ追加
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dict'}}
print(dict_sample)
print(dict_sample['four']['inner'])

# 順序を保持しないので注意
colors = {}
colors[1] = 'blue'
colors[0] = 'red'
colors[2] = 'green'
print(colors)

# .keys(), .values(): dictionaryをfor文で回せるメソッド
# 省略すると.keys()
for x in fruits_colors:
    print(x)

for color in fruits_colors.values():
    print(color)

# .items(): keyとvalueをセットにしてtupleでforを回す
# 最もよく使用される
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}.")

# dict_function
# ifで記述するケース
if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('the key is not found.')
# .get(): 安全に値を取得することができる
# 存在しないkeyの場合にdefaultの値を返す(第2op.)
# keyで指定する値がユーザからのインプットのケースに使用
fruit = input("Enter the name of the fruit.")
print(fruits_colors.get(fruit, 'Nothing'))

# .update(): dictionary同士の結合
# listの結合は+
fruits_colors_02 = {'banana': 'yellow', 'kiwi': 'green'}
fruits_colors.update(fruits_colors_02)
print(fruits_colors)

# challenge_01:
age = int(input("Wellcome to casino!! Hou old are you?"))
casino_age = 18
if not casino_age <= age:
    print(f"Entrance is not allowed to those under {casino_age}.")
    exit()
else:
    print("Please come in.")

game_dict = {'1': 'Roulette', '2': 'Blackjacke', '3': 'Poker'}
while True:
    print("Select a game-No.")
    for num, game_name in game_dict.items():
        print(f"{num}: {game_name}")
    game_no = input(": ")
    if game_no in game_dict:
        print(f"{game_dict[game_no]} is selected")
        break
    else:
        print("Error: invalid data")

