import copy
from dataclasses import dataclass
from typing import Dict, List
import json
from icecream import ic


@dataclass
class Key:
    # x/y are floats to perm
    x: float
    y: float
    code: str = None
    size: float = 1

    def copy(self):
        return copy.copy(self)

    def reflect_over_vertical_line(self, line_x: int):
        assert line_x > self.x
        dist_from_line = line_x - self.x
        reflected = copy.copy(self)
        reflected.x = line_x + dist_from_line
        return reflected

    @staticmethod
    def make_row(start_x, start_y, num_keys, key_size=1):
        return [Key(start_x + i, start_y, size=key_size) for i in range(num_keys)]

    @staticmethod
    def make_col(start_x, start_y, num_keys: int, key_size=1):
        return [Key(start_x, start_y + i, size=key_size) for i in range(num_keys)]


@dataclass
class KeyBoard:
    keys: List[Key]
    width: float
    height: float

    @staticmethod
    def from_kb_info(kb_info: Dict = None, path: str = None, layout_name="LAYOUT"):
        if not kb_info:
            with open(path) as f:
                kb_info = json.load(f)
        layout = kb_info["layouts"][layout_name]["layout"]
        keys = [Key(key["x"], key["y"]) for key in layout]
        return KeyBoard(keys, kb_info["width"], kb_info["height"])
