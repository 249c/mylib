# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)
print('lemon' in fruits)
print('melon' not in fruits)
print('h' in 'hello')

# challenge_01: フルーツがあれば取り出し、なければ仕入れる
print("before: {}".format(fruits))
favorite = input("What is your favorite fruit?")
if favorite in fruits:
    print("I'll give {} to you.".format(favorite))
    fruits.remove(favorite)
else:
    print("Sorry, {} is sold out.".format(favorite))
    fruits.append(favorite)
print("after: {}".format(fruits))