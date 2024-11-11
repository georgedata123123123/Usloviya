# Выполнил: Мальцев Георгий Павлович




def calendar_my(k):
    try:
        k = int(k)
    except ValueError:
        return 'Ошибка, вводите числа'
    else:
        match k:
            case 1|3|5|7|8|10|12: return 31
            case 2: return 28
            case 4|6|9|11: return 30
            case _: return 'Ошибка'
