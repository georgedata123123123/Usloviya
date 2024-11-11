# Выполнил: Мальцев Георгий Павлович


def calendar_2(m, d):
    try:
        d = int(d)
        m = int(m)
    except ValueError:
        return 'Ошибка, вводите числа'
    else:
        match d, m:
            case 31, 1 | 3 | 5 | 7 | 8 | 10 | 12:
                return f"1.{m + 1}"
            case 28, 2:
                print(f"1.{m + 1}")
            case 30, 4 | 6 | 9 | 11:
                print(f"1.{m + 1}")
            case d, 1|3|5|7|8|10|12 if 0 < d < 31:
                print(f"{d+1}.{m}")
            case d, 2 if 0<d<28:
                print(f"{d+1}.{m}")
            case d, 4 | 6 | 9 | 11 if 0 < d < 30:
                print(f"{d+1}.{m}")
            case _:
                print('Error')