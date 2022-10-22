salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
# Плохой способ решения
spend_1 = spend
need_money_1 = spend_1 - salary
print(need_money_1)

spend_2 = spend_1 + spend * increase  # Рост цен начинается со 2 месяца
need_money_2 = need_money_1 + spend_2 - salary
print(round(need_money_2))

spend_3 = spend_2 + spend_2 * increase
need_money_3 = need_money_2 + spend_3 - salary
print(round(need_money_3))

spend_4 = spend_3 + spend_3 * increase
need_money_4 = need_money_3 + spend_4 - salary
print(round(need_money_4))

spend_5 = spend_4 + spend_4 * increase
need_money_5 = need_money_4 + spend_5 - salary
print(round(need_money_5))

spend_6 = spend_5 + spend_5 * increase
need_money_6 = need_money_5 + spend_6 - salary
print(round(need_money_6))

spend_7 = spend_6 + spend_6 * increase
need_money_7 = need_money_6 + spend_7 - salary
print(round(need_money_7))

spend_8 = spend_7 + spend_7 * increase
need_money_8 = need_money_7 + spend_8 - salary
print(round(need_money_8))

spend_9 = spend_8 + spend_8 * increase
need_money_9 = need_money_8 + spend_9 - salary
print(round(need_money_9))

spend_10 = spend_9 + spend_9 * increase
need_money_10 = need_money_9 + spend_10 - salary
print(round(need_money_10))  # количество денег, чтобы прожить 10 месяцев

# Хороший способ решения
need_money = spend - salary  # необходимое кол-во денег для первого месяца
for i in range(1, months):
    spend += spend * increase
    need_money += spend - salary
print(round(need_money))  # количество денег, чтобы прожить 10 месяцев
