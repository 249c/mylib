# whileループ: 条件式がFalseになるまで繰り返し
count = 0
while count < 10:
    print(count)
    count += 1

# break, continue
# 条件を満たしたらbreak, そうでなければ繰り返し
while True:
    age = int(input("Hou old are you?"))
    if not 0 <= age < 120:
        print("invalid data")
        continue  # 省略可
    else:
        print(f"Your age is {age}.")
        break

# challenge_01
age = int(input("Wellcome to casino!! Hou old are you?"))
casino_age = 18
if not casino_age <= age:
    print(f"Entrance is not allowed to those under {casino_age}.")
    exit()
else:
    print("Please come in.")

game_text = """Select a game-No:
1. Roulette
2. Blackjack
3. Poker
"""
while True:
    game_no = int(input(game_text))
    if not 1 <= game_no <= 3:
        print("Error: invalid data")
    else:
        print(f"{game_no} is selected")
        break
