import sys


def phrase_сomporator(phrase1, phrase2):
    if len(phrase1) == len(phrase2):
        return 'Фразы равной длины'
    if len(phrase1) >= len(phrase2):
        return 'Фраза 1 длиннее фразы 2'
    return 'Фраза 2 длиннее фразы 1'


# print(phrase_сomporator("132313", "sjfbjsgfchsch"))
# print(phrase_сomporator("134645452313", "sjfhsch"))
# print(phrase_сomporator("134645452313", "134645452313"))


def is_leap_year(year):
    return 'Високосный год' if year % 4 == 0 else 'Обычный год'


# print(is_leap_year(1990))
# print(is_leap_year(1991))
# print(is_leap_year(1992))


def determine_zodiac_sign():

    try:
        zodiac_signs = {
            'январь': {
                'startDate': 20,
                'zodiacs': ['Козерог', 'Водолей']
            },
            'февраль': {
                'startDate': 20,
                'zodiacs': ['Водолей', 'Рыбы']
            },
            'март': {
                'startDate': 21,
                'zodiacs': ['Рыбы', 'Овен']
            },
            'апрель': {
                'startDate': 21,
                'zodiacs': ['Овен', 'Телец']
            },
            'май': {
                'startDate': 21,
                'zodiacs': ['Телец', 'Близнецы']
            },
            'июнь': {
                'startDate': 22,
                'zodiacs': ['Близнецы', 'Рак']
            },
            'июль': {
                'startDate': 23,
                'zodiacs': ['Рак', 'Лев']
            },
            'август': {
                'startDate': 23,
                'zodiacs': ['Лев', 'Дева']
            },
            'сентябрь': {
                'startDate': 23,
                'zodiacs': ['Дева', 'Весы']
            },
            'октябрь': {
                'startDate': 23,
                'zodiacs': ['Весы', 'Скорпион']
            },
            'ноябрь': {
                'startDate': 22,
                'zodiacs': ['Скорпион', 'Стрелец']
            },
            'декабрь': {
                'startDate': 21,
                'zodiacs': ['Стрелец', 'Козерог']
            },
        }

        day = int(input('Введите день:\n'))
        month = input('Введите месяц:\n')

        zodiac_data = zodiac_signs.get(month.lower())
        zodiacs = zodiac_data.get('zodiacs')
        startDate = zodiac_data.get('startDate')

        return zodiacs[0] if startDate > day else zodiacs[1]

    except:

        return 'Unexpected error: {error}'.format(error=sys.exc_info()[0])


# print(determine_zodiac_sign())


def get_package():
    width = int(input('width = '))
    length = int(input('length = '))
    height = int(input('height = '))

    if width < 15 and length < 15 and height < 15:
        return 'Коробка №1'

    if width in range(15, 50) or length in range(15, 50) or height in range(15, 50):
        return 'Коробка №2'

    if length > 200:
        return 'Упаковка для лыж'

    return 'Стандартная коробка №3'


# print(get_package())


def is_lucky_ticket(ticket_number):
    signs = [1, 1, 1, -1, -1, -1]
    result = 0
    for index, digit in enumerate(str(ticket_number), start=0):
        result += int(digit) * signs[index]
    return 'Счастливый билет' if result == 0 else 'Несчастливый билет'


# print(is_lucky_ticket(123456))
# print(is_lucky_ticket(222114))


