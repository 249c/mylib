# mutable: 変更可能なオブジェクト(list, dict, set)
# データサイズが大きくなりがちなデータ型, メモリ節約
fruits = ['apple', 'peach', 'banana']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('lemon')
print(fruits)
print(f"fruitsのIDは{id(fruits)}")  # Same ID


# immutable: 変更不可のオブジェクト(int, float, str, bool, tuple)
fruit = 'apple'
print(f"fruitのIDは{id(fruit)}")
fruit += ', lemon'
print(fruit)
print(f"fruitのIDは{id(fruit)}")  # Different ID

# forループで文字列を末尾に追記 -> メモリを使い回せないので非効率
# 実際は可能な限り効率を考慮した処理が実行される
text = ""  # 1-2-3-4-5-6-7-...
for i in range(1, 11):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
print(text)

# listとjoinを使ったメモリ効率の良いコーディング例
text_list = []
for i in range(1, 11):
    text_list.append((str(i)))
text = "-".join(text_list)
print(text)