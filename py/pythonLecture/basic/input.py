# input(): ユーザの入力した値(文字列)を取得する

# age = input("あなたは何歳ですか？")  # intでなくstrで受け取っている点に注意
# print("あなたは {} 歳です".format(age))

# Challenge_01: 18歳以上で入場できるカジノ
casino_age = 18
age = int(input("How old are you?"))  # 文字列から数字へ変換
print("You are {} years old.".format(age))

if age >= casino_age:
    print("Please come in.")
else:
    print("Entrance is not allowed to those under {}.".format(casino_age))
    exit()

# Challenge_02: ゲームを選択
game_text = """Select a game-No.
1. Roulette
2. Blackjack
3. Poker
"""
game = int(input(game_text))
if not 1 <= game <= 3:
    print("invalid value")
else:
    print("{} is selected".format(game))