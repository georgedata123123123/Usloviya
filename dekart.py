# Выполнил: Мальцев Георгий Павлович


def dekart(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return 'Используйте числа!'
    else:
        if (x >= 0) & (y >=0):
            return 'Четверть 1'
        if (x <= 0) & (y >= 0) :
            return 'Четверть 2'
        if (x <= 0) & (y <= 0) :
            return 'Четверть 3'
        if (x >= 0) & (y <= 0) :
            return 'Четверть 4'