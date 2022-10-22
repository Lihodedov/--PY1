money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
# Плохой способ решения
spend_1 = spend + spend * increase  # расходы за 1 месяц с учетом роста цен
money_1 = (money_capital + salary) - (spend + spend * increase)  # ЗП за 1 месяц минус расходы с учетом роста цен
print("Оставшиеся деньги через 1 месяц = ", money_1)

spend_2 = spend_1 + spend_1 * increase
money_2 = money_1 + salary - spend_2
print("Оставшиеся деньги через 2 месяца = ", money_2)

spend_3 = spend_2 + spend_2 * increase
money_3 = money_2 + salary - spend_3
print("Оставшиеся деньги через 3 месяца = ", money_3)

spend_4 = spend_3 + spend_3 * increase
money_4 = money_3 + salary - spend_4
print("Оставшиеся деньги через 4 месяца = ", round(money_4, 0))

spend_5 = spend_4 + spend_4 * increase
money_5 = money_4 + salary - spend_5
print("Оставшиеся деньги через 5 месяцев = ", round(money_5, 0))

spend_6 = spend_5 + spend_5 * increase
money_6 = money_5 + salary - spend_6
print("Оставшиеся деньги через 6 месяцев = ", round(money_6, 0))
# на 6 месяц денег уже не хватит, расходы превысили доходы


# Хороший способ решения
while (spend + spend * increase) <= (money_capital + salary - spend):
    month += 1
    spend += spend * increase
print(month)
