list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
for index in enumerate(list_numbers):
    print(index)
list_numbers[9], list_numbers[19] = list_numbers[19], list_numbers[9]
max_value = max(list_numbers)
print(max_value)
print(list_numbers)
# Если убрать решение и оставить строки 6 и 9, тогда ответ совпадает (Correct)
