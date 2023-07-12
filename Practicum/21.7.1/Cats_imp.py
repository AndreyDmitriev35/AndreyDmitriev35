from Cats_main import Cat

cat_1 = Cat("Кошак", "мальчик", 3)
cat_2 = Cat("Мурка", "девочка", 5)

print(f"Первая кошка\nИмя: {cat_1.getname()}\nПол: {cat_1.getgender()}\nВозраст: {cat_1.getage()}\n")
print(f"Вторая кошка\nИмя: {cat_2.name}\nПол: {cat_2.gender}\nВозраст: {cat_2.age}")