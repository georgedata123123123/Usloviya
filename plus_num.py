# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def plus_num(a: int, b: int, c: int):
    try:
        t = 0
    except ValueError:
        print('Используйте числа!')
        logging.info("Вели неверное значение")
    else:
        if a > 0:
            t += 1
        if b > 0:
            t += 1
        if c > 0:
            t += 1
        return f"Ответ: {t}"
        logging.info("Success!")

