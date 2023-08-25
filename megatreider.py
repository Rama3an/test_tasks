from itertools import combinations

n, m, s = map(int, input().split())


data = input().split()


dict_profit = dict()
dict_price = dict()

while data:
    dict_profit[f"{' '.join(data)}"] = 30 * int(data[3]) + ((int(data[3]) * 1000) - (float(data[2]) * 10 * int(data[3])))
    dict_price[f"{' '.join(data)}"] = float(data[2]) * 10 * int(data[3])
    data = input().split()


arr_profit = []
for i in range(1, len(dict_profit) + 1):
    arr_profit.extend(list(combinations(dict_profit, i)))


max_profit = 0
arr_lot = []

for i in arr_profit:
    profit_tuple = 0
    price_tuple = 0
    arr_lot_tuple = []
    for j in i:
        arr_lot_tuple.append(j)
        profit_tuple += dict_profit[j]
        price_tuple += dict_price[j]
    if profit_tuple > max_profit and price_tuple <= s:
        max_profit = profit_tuple
        arr_lot = arr_lot_tuple.copy()

print(max_profit)
for i in range(len(arr_lot) + 1):
    if i == len(arr_lot):
        print()
    else:
        result = arr_lot[i]
        print(result)

