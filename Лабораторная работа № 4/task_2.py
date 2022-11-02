def get_count_char(str_):
    lower_ = str_.lower()
    stroka_ = "".join(lower_.split())
    simvol_dict = {}
    for simvol in stroka_:
        if simvol.isalpha():
            if simvol in simvol_dict:
                simvol_dict[simvol] += 1
            else:
                simvol_dict[simvol] = 1
    return simvol_dict
#  TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

