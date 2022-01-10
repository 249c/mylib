# tuple: 変更できないリスト（[]でなく()を使用）
# 値を変更する必要のないリストに使う

# Not tuple -> Updatable
date_of_birth = [1990, 1, 3]
date_of_birth[0] = 1999
print(date_of_birth)

# tuple -> Error(Update is not available)
# date_of_birth = (1990, 1, 3)
# date_of_birth[0] = 1999  # error
# print(date_of_birth)

# Unpack <- tuple
# アンパック処理はリストでなくタプル型で
year, month, date = date_of_birth
print(f"year:{year}, month:{month}, date:{date}")