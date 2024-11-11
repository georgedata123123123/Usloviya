# Выполнил: Мальцев Георгий Павлович

import logging

logging.basicConfig(level=logging.INFO, filename="py_log_6.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def marks(k):
    try:
        k = int(k)
    except ValueError:
        return 'Ошибка, вводите числа'
        logging.info('Ввели не число')
    else:
        match k:
            case 1: return 'плохо'
            case 2: print('неудовлетворительно')
            case 3: print('удовлетворительно')
            case 4: print('хорошо')
            case 5: print('отлично')
            case _: print('Ошибка')
        logging.info('Успех!')


