salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
need_money += spend - salary  # количество денег, чтобы прожить 1 месяц
for i in range(2, months + 1):  # количество денег, чтобы прожить с 2 по 10 месяц
    spend += spend * increase
    need_money += spend - salary
print(round(need_money)) 
