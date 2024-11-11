# Выполнил: Мальцев Георгий Павлович

def robot_2(o, a, b):
    try:
        o = str(o)
        a = int(a)
        b = int(b)
    except ValueError:
        return print('Ошибка, вводите числа и строки где необходимо')
    else:
        match o:
            case '*': print(a*b)
            case '/': print(a/b)
            case '-': print(a-b)
            case '+': print(a+b)
            case _: print('Неизвестный оператор')
