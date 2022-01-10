# forループ
# iteration, iterable
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f"I live {fruit}!!")

for char in "hello world!!":
    print(f"char: {char}")

# challenge_01:
favorite = input("What's your favorite fruit?")
for fruit in fruits:
    if fruit == favorite:
        print(True)
    else:
        print(False)

# challenge_02:
favorite_fruits = []
dislike_fruits = []
for fruit in fruits:
    answer = input(f"Do you like {fruit}? Answer with a y/n: ")
    if answer == "yes":
        favorite_fruits.append(fruit)
    else:
        dislike_fruits.append(fruit)
print(f"Your favorite fruits are {favorite_fruits}.")
print(f"Your dislike fruits are {dislike_fruits}.")
