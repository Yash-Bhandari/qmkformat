from typing import List
from qmkformat.parser import read_and_parse_layout

rows = [12, 12, 12, 14, 6]

lines = read_and_parse_layout("old.c")

# left + bottom junction
lb_junction = '┐'
# bottom + top junction
lbt_junction = '┤'
# left + right + bottom + top junction
lrbt_junction ='┼'
# left + top junction
lt_junction = '┘'
rt_junction = '└'
rb_junction = '┌'
rbt_junction = '├'


def cell_line(width=9) -> str:
    return '─'*width

cell_line()

class StringFormatter:
    def __init__(self, layouts: List[List[str]], cell_width=9):
        self.layouts = layouts

    def format_layout(self):
        for layout in self.layouts:
            pass
