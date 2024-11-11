# Выполнил: Мальцев Георгий Павлович


def sravv(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print('Используйте числа!')
    else:
        if a <= b:
            return b
        else:
            return a
