import string
import random


def get_random_password() -> str:
    values = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = str(random.sample(values, 8))
    return password


print(get_random_password())
