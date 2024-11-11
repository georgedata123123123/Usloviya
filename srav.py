# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log_2.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def srav(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return 'Используйте числа!'
        logging.info("Вели неверное значение")
    except Exception:
        return 'Что-то пошло не так'
        logging.error("Что-то не так?")
    else:
        if a <= b:
            return b
        else:
            return a
        logging.info("Success!")
