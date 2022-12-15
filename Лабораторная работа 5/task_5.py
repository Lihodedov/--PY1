import string
import random


def get_random_password(n: int) -> str:
    """
    Функция генерирует случайные пароли заданной длины

    :param n: Длинна случайного пароля
    :return: Случайный пароль заданной длины
    """
    values = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = str(random.sample(values, n))
    return password


print(get_random_password(8))  # по умолчанию 8 символов
