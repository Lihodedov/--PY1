def get_count_char(str_):
    lower_ = str_.lower()
    simvol_dict = {}
    for simvol in lower_:
        if simvol.isalpha():
            if simvol in simvol_dict:
                simvol_dict[simvol] += 1
            else:
                simvol_dict[simvol] = 1
    return simvol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

dict_ = get_count_char(main_str).copy()

def percent(slovar):
    values_ = dict_.values()
    sum_ = sum(values_)
    for name, value in dict_.items():
        value_ = round(value / sum_ * 100, 2)
        print({name: value_})


print (percent(dict_))

