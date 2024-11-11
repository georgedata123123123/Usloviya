# Выполнил: Мальцев Георгий Павлович

def chislo(d):
    try:
        d = int(d)
        if (100>d) or (d>999):
            raise ValueError
    except ValueError:
        return 'Ошибка, вводите числа от 100 до 999'
    else:
        match  d // 100:
            case 1: a='сто'
            case 2: a='двести'
            case 3: a='триста'
            case 4: a='четыресто'
            case 5: a='пятьсот'
            case 6: a='шестьсот'
            case 7: a='семьсот'
            case 8: a='восемьсот'
            case 9: a='девятьсот'
        match (d % 100) // 10:
            case 2: a = a + ' двадцать'
            case 3: a = a + ' тридцать'
            case 4: a = a + ' сорок'
            case 5: a = a + ' пятьдесят'
            case 6: a = a + ' шестьдесят'
            case 7: a = a + ' семьдесят'
            case 8: a = a + ' восемьдесят'
            case 9: a = a + ' девяносто'
            case 1 if d % 100 == 10:
                a = a + ' десять'
                return a
            case 1 if d % 100 == 11:
                a = a + ' одинадцать'
                return a
            case 1 if d % 100 == 12:
                a = a + ' двенадцать'
                return a
            case 1 if d % 100 == 13:
                a = a + ' тринадцать'
                return a
            case 1 if d % 100 == 14:
                a = a + ' четырнадцать'
                return a
            case 1 if d % 100 == 15:
                a = a + ' пятнадцать'
                return a
            case 1 if d % 100 == 16:
                a = a + ' шестнадцать'
                return a
            case 1 if d % 100 == 17:
                a = a + ' семнадцать'
                return a
            case 1 if d % 100 == 18:
                a = a + ' восемнадцать'
                return a
            case 1 if d % 100 == 19:
                a = a + ' девятнадцать'
                return a
        match d % 10:
            case 1: a = a + ' один'
            case 2: a = a + ' два'
            case 3: a = a + ' три'
            case 4: a = a + ' четыре'
            case 5: a = a + ' пять'
            case 6: a = a + ' шесть'
            case 7: a = a + ' семь'
            case 8: a = a + ' восемь'
            case 9: a = a + ' девять'
        return a

