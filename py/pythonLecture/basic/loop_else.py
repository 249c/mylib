fruits = ['apple', 'peach', 'melon', 'grapes']

for fruit in fruits:
    ans = input(f"Is {fruit} the fruit you're looking for? y/n: ")
    if ans == "y":
        print("End the loop.")
        break
    else:
        print("next question.")
else:
    print("The fruit you were looking for was not found.")

# while else
count = 0
while count < 10:
    print (count)
    count += 1
else:
    print("End of loop")

# challenge_01:
balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"Would you like to participate in a game that costs {game_price} yen each?(balance: {balance} yen)(y/n?): ")
    if choice == "y":
        balance -= game_price
        print(balance)
    elif choice == "n":
        print("Thanks for playing!!")
        break
    else:
        print("Please answer with y/n.")
else:
    print(f"Error: Your balance is insufficient.( {balance} yen )")
