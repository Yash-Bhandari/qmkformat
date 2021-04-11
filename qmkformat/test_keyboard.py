import pytest
from qmkformat.keyboard import Key, KeyBoard


def test_reflect_over_vertical_line_does_not_modify_original():
    key = Key(3, 2)
    reflected = key.reflect_over_vertical_line(10)
    assert id(reflected) != id(key)
    assert key.x == 3


@pytest.mark.parametrize("x,line_x,expected_x", [(0, 2, 4), (1, 4, 7)])
def test_reflect_over_vertical_line(x, line_x, expected_x):
    key = Key(x, 2)
    assert key.reflect_over_vertical_line(line_x).x == expected_x


def test_make_row():
    keys = Key.make_row(1, 2, 2)
    assert keys == [Key(1, 2), Key(2, 2)]


def test_make_col():
    keys = Key.make_col(0, 0, 3)
    assert keys == [Key(0, 0), Key(0, 1), Key(0, 2)]


def test_from_kb_info_file():
    keyboard = KeyBoard.from_kb_info(path='keyboards/iris_rev4.json')
    assert len(keyboard.keys) == 56
    first_key = keyboard.keys[0]
    assert first_key.x == 0
    assert first_key.y == 0.375