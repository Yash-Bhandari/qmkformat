from typing import List
from qmkformat.parser import read_and_parse_layout
from qmkformat.keyboard import Keyboard
from dataclasses import dataclass

rows = [12, 12, 12, 14, 6]

lines = read_and_parse_layout("old.c")

# left + bottom junction
lb_junction = "┐"
# left + bottom + top junction
lbt_junction = "┤"
# left + right + bottom + top junction
lrbt_junction = "┼"
# left + top junction
lt_junction = "┘"
rt_junction = "└"
rb_junction = "┌"
rbt_junction = "├"

junction_map = {
    "1010": lb_junction,
    "1011": lbt_junction,
    "1111": lrbt_junction,
    "1001": lt_junction,
    "0101": rt_junction,
    "0110": rb_junction,
    "0111": rbt_junction,
}


def cell_line(width=9) -> str:
    return "─" * width


@dataclass
class LineSegment:
    left: bool = False
    right: bool = False
    bottom: bool = False
    top: bool = False
    mid: bool = False

    def draw(self, width):
        line = self.get_starting_junction()

    def get_starting_junction(self):
        # we encode the state as a binary string for concise comparision
        state = "".join(
            int(binary) for binary in [self.left, self.right, self.bottom, self.top]
        )
        if state not in junction_map:
            raise Exception("Invalid LineSegment state", self)
        return junction_map[state]


class StringFormatter:
    def __init__(
        self, layout_key_codes: List[List[str]], keyboard: Keyboard, cell_width=9
    ):
        self.layouts = [
            keyboard.create_layout(key_codes) for key_codes in layout_key_codes
        ]

    def prepare_coordinates(self, layout: Keyboard):
        for y, row in layout.rows.items():
            line=[]
            # iterate through keys, left to right
            for key in sorted(row, key=lambda key: key.col):
                line_seg = LineSegment()
                # Not the top row or there is a row above
                if key.row != 0 or key.row - 1 in layout.rows:
                    line_seg.top = True
                line.append(line_seg)

    def format_layout(self, layout: Keyboard):
        for row in layout.rows:
            pass


