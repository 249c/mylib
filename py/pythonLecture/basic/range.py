# range(start, stop, step)
# startの省略値: 0
# stepの省略値: 1

# 連番を出力
for i in range(7):
    print(i)
# 指定回数分出力
# iは使用しないためアンダースコアに
for _ in range(3):
    print("hello")

# challenge_01: multiple of 3, 5, 15
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
