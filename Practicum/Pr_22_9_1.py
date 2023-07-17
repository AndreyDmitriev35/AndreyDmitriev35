number_list = []
random_number = None
while not number_list:
    try:
        number_list = list(map(int, input("Введите целые числа через проблел:").split()))
    except ValueError:
        print("Вы ввели неверные значения")
while not random_number:
    try:
        random_number = int(input("Введите любое целое число:"))
        if random_number > max(number_list) or random_number < min(number_list):
            print("Введенное число находится за рамками списка")
            random_number = None
        # elif random_number not in number_list:
        #     print("Введенное число не входит в список чисел")
        #     random_number = None
    except ValueError:
        print("Вы ввели неверные значения")


# Функция сортировки
def sort_list():
    for i in range(len(number_list)):
        for j in range(len(number_list)-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    return number_list


number_list = sort_list()


# Двоичный поиск
def binary_search(number_list, random_number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if number_list[middle] == random_number:
        return middle
    elif number_list[middle - 1] < random_number < number_list[middle]:
        return middle
    elif random_number < number_list[middle]:
        return binary_search(number_list, random_number, left, middle - 1)
    else:
        return binary_search(number_list, random_number, middle + 1, right)


left_index = binary_search(number_list, random_number, 0, len(number_list))-1
right_index = binary_search(number_list, random_number, 0, len(number_list))

print("Отсортированный список:", number_list)
print("Индекс меньше введенного числа:", left_index)
print("Индекс больше введенного числа или равен ему:", right_index)
