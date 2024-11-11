# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def srav_min(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        return 'Используйте числа!'
        logging.info("Вели неверное значение")
    else:
        if a<=b<=c:
            return a
        elif a<=c<=b:
            return a
        elif c<=b:
            return c
        else:
            return b