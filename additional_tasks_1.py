# Словарь типов багов
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

# Словарь со списками идентификаторов багов
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}

#функция удаляет дубли из списков с тикетами
def delete_duplicates(tickets):
    new_ticket = {}
    for number, ticket in tickets.items():
        new_ticket[number] = list(set(ticket)) # убираем дубликаты
    return new_ticket

#функция связывает уровень критичности со списком уникальных тикетов
def level_ratio(types, tickets):
    new_ticket = delete_duplicates(tickets)
    tickets_by_type = {}
    seen_tickets = set()

    for number, type in types.items():
        tickets_by_type[type] = []

        for ticket in new_ticket[number]:
            if ticket not in seen_tickets:
                tickets_by_type[type].append(ticket)
                seen_tickets.add(ticket)

    return tickets_by_type

# Результат работы функции сохраняем в переменную result
result = level_ratio(types, tickets)
# Выводим полученный результат
print(result)