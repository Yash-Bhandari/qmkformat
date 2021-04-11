import pytest
from qmkformat.keyboard import Key, Keyboard


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


def test_create_kb_from_iris_info_file_has_correct_keys(iris: Keyboard):
    assert len(iris.keys) == 56
    first_key = iris.keys[0]
    assert first_key.x == 0
    assert first_key.y == 0.375
    last_key = iris.keys[len(iris.keys) - 1]
    assert last_key.x == 10.5
    assert last_key.y == 4.25


def test_create_kb_from_iris_info_file_has_correct_cols(iris: Keyboard):
    # 2 * (6 main columns per half, plus 4 staggered columns for the thumb keys)
    assert len(iris.cols) == 10 * 2
    assert len(iris.cols[0]) == 4
    assert len(iris.cols[4]) == 4
    assert len(iris.cols[3.5]) == 1
    assert len(iris.cols[4.5]) == 1
    assert_cols_are_symmetric(iris, 7)


def assert_cols_are_symmetric(keyboard: Keyboard, center_x):
    """
    Checks that column lengths are symmetric about the center_x. 
    Useful for symmetric keyboards.
    """
    for x in sorted(keyboard.cols):
        # only have to check the first half
        if x > keyboard.width / 2:
            break
        opposite_col_x = center_x + (center_x - x)
        assert len(keyboard.cols[x]) == len(keyboard.cols[opposite_col_x])


def test_create_kb_from_iris_info_file_has_correct_rows(iris: Keyboard):
    assert len(iris.rows) == 5
    assert len(iris.rows[0]) == 6 * 2
    assert len(iris.rows[3]) == 7 * 2
    assert len(iris.rows[4]) == 3 * 2
