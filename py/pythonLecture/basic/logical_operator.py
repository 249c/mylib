# 論理演算子(logical operators)
# and, or, not
a = 1
b = 1
c = 10
d = 100

# and: True * True のみTrue
print(a == b and c < d)  # True(T*T)
print(a == b and c > d)  # False(T*F)
print(a != b and c < d)  # False(F*T)
print(a != b and c > d)  # False(F*F)

# or:　False * False のみ False
print(a == b or c < d)  # True(T*T)
print(a == b or c > d)  # True(T*F)
print(a != b or c < d)  # True(F*T)
print(a != b or c > d)  # False(F*F)

# Challenge_01: 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 13
height = 140
print(age >= 10 and height >= 110)

# Challenge_02: 修士号保持もしくは5年以上実務経験があればVisa取得可
master = False
job_experience = 6
print(master or job_experience >= 5)
