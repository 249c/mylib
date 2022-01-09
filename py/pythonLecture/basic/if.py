# if文
# 飲酒は20歳以上でOK
age = 19
age_alcohol = 20
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have driver's license")

if not 0 < age < 120:
    print("The value is invalid")

# Challenge_01: ATM引き出し
balance = 3000000
withdraw = 1300000
# if balance > withdraw:
#     balance -= withdraw
#     print("Your new balance is {}".format(balance))
# else:
#     print("You don't have money")

# Challenge_02: 引き出し条件100万まで
withdrawal_limit = 1000000
if withdraw > withdrawal_limit:
    print("Error: The withdrawal limit is {}".format(withdrawal_limit))
elif balance > withdraw:
    balance -= withdraw
    print("Your new balance is {}".format(balance))
else:
    print("You don't have money")

# if文のNoneの取り扱い
a = None  # aには何も値が入っていない
# if a is None:
#     print("a is None")
# else:
#     print("a has value")

if a:
    print("a has value")
else:
    print("a is None")

# Noneなら値を代入
if not a:
    a = 10
