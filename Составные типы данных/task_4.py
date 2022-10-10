list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2  # TODO поделить количество игроков пополам

left_team = list_players[:middle_index]  # TODO взять левую половину списка
right_team = list_players[middle_index:]  # TODO взять правую половину списка

print(left_team)
print(right_team)
