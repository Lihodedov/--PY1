money_capital = 10000  # финансовая подушка безопасности
salary = 5000  # зарплата
spend = 6000  # траты
increase = 0.05  # рост цен

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
i = money_capital - spend + salary  # кол-во денег через один месяц
while i >= spend:
    i += salary - spend
    spend += spend * increase
    month += 1
print(month)
