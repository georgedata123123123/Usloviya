from pytest import mark
from plus_num import plus_num
from srav import srav
from sravv import sravv
from srav_min import srav_min
from dekart import dekart
from marks import marks
from calendar_my import calendar_my
from calendar_2 import calendar_2
from calendar_3 import robot
from chislo import chislo
from robot_2 import robot_2



def test_plus_num():
    assert plus_num(1, 2,3) == f"Ответ: 3"

@mark.parametrize("result, a, b", [('Используйте числа!', 'f', 3), (10, 10, 10)])
def test_srav(result, a, b):
    assert srav(a, b) == result



def test_sravv_pos():
    assert sravv(5, 3) == 5

def test_sravv_neg(capsys):
    sravv('r', 4)
    captured = capsys.readouterr()
    assert captured.out == 'Используйте числа!\n'

@mark.parametrize("result, a, b, c", [('Используйте числа!','f',2, 3), (1, 1, 2, 3)])
def test_srav_min(result, a, b, c):
    assert srav_min(a, b, c) == result

@mark.parametrize("result, x, y", [('Используйте числа!', 'f', 3), ('Четверть 1', 1, 2)])
def test_dekart(result, x, y):
    assert dekart(x, y) == result

@mark.parametrize("result, k", [('Ошибка, вводите числа', 'f'), ('плохо', 1)])
def test_mark(result, k):
    assert marks(k) == result

@mark.parametrize("result, k", [('Ошибка, вводите числа', 'f'), (31, 12)])
def test_calendar(result, k):
    assert calendar_my(k) == result

@mark.parametrize("result, m, d", [('Ошибка, вводите числа', 'f', 4), ('1.2', 1, 31)])
def test_calendar_2(result, m, d):
    assert calendar_2(m, d) == result

@mark.parametrize("result, a, b", [('Ошибка ввода!\n', 'f', 4), ('В\n', 'Ю', 1)])
def test_calendar_3(result, a, b, capsys):
    robot(a, b)
    captured = capsys.readouterr()
    assert captured.out == result

@mark.parametrize("result, d", [('Ошибка, вводите числа от 100 до 999', 'f'), ('сто десять', 110)])
def test_chislo(result, d):
    assert chislo(d) == result

@mark.parametrize("result, o, a, b", [('Ошибка, вводите числа и строки где необходимо\n', 'f', 4, 'ggg'), ('Неизвестный оператор\n', 'f', 4, 5)])
def test_robot_2(result, o, a, b, capsys):
    robot_2(o, a, b)
    captured = capsys.readouterr()
    assert captured.out == result