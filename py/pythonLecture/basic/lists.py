# リスト(lists): 複数のオブジェクトを順序付けて保存するデータ型
# []で括って、カンマで各オブジェクトを区切る
# indexは0からスタート, ラストから-1, -2,...
fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]
print(hetro_list)
print(fruits[0])
print(fruits[-1])
print(hetro_list[-1][2])

# 文字列操作も可
print("hello world"[4])

# .append: 新しいオブジェクトを追加(リストの一番最後)
print(fruits)
fruits.append('banana')
print(fruits)

# .insert: 指定したindexに指定したオブジェクトを追加
fruits.insert(3, 'lemon')
print(fruits)

# .remove: マッチした最初のオブジェクトを除く
fruits.remove('peach')
print(fruits)

# .sort: 並び替え
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# len(): リストの要素数を取得
print(len(fruits))
print(len("hello world"))

# slicing: 「:」を使って複数の要素を取得
# 基本は[開始idx:未満idx], 省略すると先頭から/末尾まで
even = [2, 4, 6, 8, 10, 12]
print(even[1:4])
print(even[:3])
print(even[3:5])
print(even[3:-1])
print(even[3:])
print("hello world"[4:])

# 全要素を取得
print(even[:])

# [開始:未満:step]
print("hello world"[2:10:2])

# 逆に並び替え
print("hello world"[::-1])

# "+"でリスト同士を結合
print([1, 2, 3] + [4, 5, 6])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# appendとの違い
a.append(b)
print(a)

# join: 要素の結合
print(" ".join(["Hi", "My", "Name", "is", "John"]))

# split: 要素に分割
# 半角スペースの場合は「" "」省略可
print("Hi My Name is John".split())
# ファイル名から拡張子を除く
filename = "sample.py"
print(filename.split(".")[0])
# 拡張子のみ取得
print(filename.split(".")[-1])
