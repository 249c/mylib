# casting: データ型の変換
# strings: '1'
# int: 1
# float: 1.5
# boolean: True, False
# list: [1, 2, 3, 4, 5]
# tuple: (1, 2, 3)
# dictionary: {"one": 1, "two": 2, "three": 3}
# set: {1, 2, 3, 4, 5}

# str(), int(), float(), list(), bool(), tuple(), set()
a = str(1)
print(f"value: {a}, type: {type(a)}")
print(f"value: {'1' + a}, type: {type('1' + a)}")
a = int('1')
print(f"value: {a}, type: {type(a)}")
print(f"value: {1 + a}, type: {type(1 + a)}")
a = float("1")
print(f"value: {a}, type: {type(a)}")
a = list("hello")
print(f"value: {a}, type: {type(a)}")
a = bool(1)
print(f"value: {a}, type: {type(a)}")
a = tuple([1, 2, 3, 4, 5])
print(f"value: {a}, type: {type(a)}")
a = set([1, 2, 3, 3, 4, 5, 5, 5])
print(f"value: {a}, type: {type(a)}")