# is演算子:同じオブジェクトかどうかを判定
a = 1
b = 1
c = 3
d = 1

print(id(1))
print(id(a))
print(id(b))

print(a is b)
print(a is not c)
print(d is a)

# Noneかどうかの判定によく使う
nothing = None
print(nothing)
print(nothing is None)
print(id(None))