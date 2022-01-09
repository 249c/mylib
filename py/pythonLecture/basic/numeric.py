# 数値型(Numeric):integer, float, complex

# int(integer, 整数) -3, 0, 2, 100
print(type(-100))

# float(浮動小数点)
print(type(0.1))

# Numeric Operator(数値演算子)
# 四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5*6 - 3/6)

result = 1 + 1.0
print(result)
print(f"type of result:{result} is {type(result)}")

# その他の演算
# floor division
print(14 // 3)  # 商
print(14 % 3)  #　modulo, 剰余, 余り
print(2 ** 3)  #　exponentiation, べき乗

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f"remain hit point is {remain}")

# augmented assignment: +=, -=, *=, /=
a = 1
# a = a + 1
a += 1
print(a)