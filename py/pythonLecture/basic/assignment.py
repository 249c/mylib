# 「ctl + /」　でコメントアウト
# 変数へ代入:assignment

hello = "Hello"
world = "World!!"
print(hello + world)

# 変数の命名規則
# snake_case
# 文字から始まる
# 文字, 数字, _
# Case sensitive(大文字と小文字を区別）

# 文字列を補完:format
print("hi {}".format("world"))
print("{} {}".format(hello, world))
# []:bracket
# {}:curly bracket
# #:pound mark

name = "John"
print("Hey, {}!! How are you doing?".format(name))
print(f"Hey, {name}!! How are you doing?")

# 変数の中身を確認したいときにも使う
balance = 100
print("balance: {}".format(balance))
print(f"balance: {balance}")

# fstring
# formatよりも内部的に速い処理しているので推奨、ver3.5より実装
print(f"{hello} {world}")
