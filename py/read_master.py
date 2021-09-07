import openpyxl

wb = openpyxl.load_workbook("Customer_master.xlsx")
ws = wb["Sheet1"]

# マスタの全データリスト
customer_list = []

# マスタの全行を1行ずつ読み込む
for row in ws.iter_rows(min_row=2):
    # 顧客IDのセルが空になったら終了
    if row[0].value is None:
        break
    # 1行分のセルの値
    value_list = []
    for c in row:
        value_list.append(c.value)
    # 1件分の顧客データを追加
    customer_list.append(value_list)

# 確認
for customer in customer_list:
    print(customer)
