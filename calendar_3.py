# Выполнил: Мальцев Георгий Павлович


def robot(a, b):
    try:
        a = str(a)
        b = int(b)
    except ValueError:
        print('Ошибка, вводите числа и строки где необходимо')
    else:
        match a, b:
            case 'С', 0: print('С')
            case 'З', 0: print('З')
            case 'Ю', 0: print('Ю')
            case 'В', 0: print('В')
            case 'С', 1: print('З')
            case 'З', 1: print('Ю')
            case 'Ю', 1: print('В')
            case 'В', 1: print('С')
            case 'С', -1: print('В')
            case 'З', -1: print('С')
            case 'Ю', -1: print('З')
            case 'В', -1: print('Ю')
            case _: print('Ошибка ввода!')
