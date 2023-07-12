quantity = int(input("Введите количество билетов: "))
print("Возраст посетителей:")
age = [int(input()) for i in range(quantity)]
price = []
for i in age:
    if i < 18:
        price.append(0)
    elif 18 <= i < 25:
        price.append(990)
    else:
        price.append(1390)
if quantity > 3:
    total_price = sum(price) - sum(price) * 0.1
    print("Сумма к оплате с учетом скидки:", int(total_price))
else:
    total_price = sum(price)
    print("Сумма к оплате:", int(total_price))
