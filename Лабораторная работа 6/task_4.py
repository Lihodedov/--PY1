import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str) -> list[dict]:
    """
       Функция реализует конвертер из csv в json

       :param filename: Файл, из которого берем данные
       :return: Список словарей
       """
    list_ = []
    with open(filename) as file:
        first_line = True
        for line in file:
            if first_line:
                name = "".join(line.split()).split(',')
                first_line = False
            else:
                values = "".join(line.split()).split(',')
                list_.append({name[i]: values[i] for i in range(0, len(name))})
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
