per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
deposit_list = list(per_cent.values())
deposit = list(map(lambda x: int(money * x / 100), deposit_list))
print(deposit)
print("Максимальная сумма, которую вы сожете заработать -",max(deposit))