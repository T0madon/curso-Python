# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))

# MONTHRANGE -> ÚLTIMO DIA
# dia, num = calendar.monthrange(2022, 12)
# print(dia, num)

# print(list(calendar.day_name))
# print(calendar.day_name[dia])

# print(calendar.weekday(2022, 12, num))

# CRIAR UM CALENDÁRIO

# print(calendar.monthcalendar(2025,1))
# [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]]

for week in calendar.monthcalendar(2025, 1):
    for day in week:
        if day == 0:
            continue
        print(day)