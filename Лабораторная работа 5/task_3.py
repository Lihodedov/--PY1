import random


def get_unique_list_numbers(a: int, b: int, c: int) -> list[int]:
    """
    Функция, которая возвращает список, заполненный случайными целыми числами. Числа в списке уникальные.

    :param a: Левая граница диапазона случайных чисел
    :param b: Правая граница диапазона случайных чисел
    :param c: Размер списка случайных чисел
    :return: Список, заполненный случайными целыми числами (уникальными)
    """
    unique_list_numbers = random.sample(range(a, b), c)
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
