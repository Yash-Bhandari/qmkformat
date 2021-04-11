import copy
import json
import math
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

from icecream import ic


@dataclass
class Key:
    """Represents a key"""

    # x/y are floats to perm
    x: float
    y: float
    code: str = None
    size: float = 1
    row: float = None
    col: float = None

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
class Keyboard:
    keys: List[Key]
    width: float
    height: float
    rows: Dict[int, List[Key]] = None
    cols: Dict[int, List[Key]] = None

    @staticmethod
    def from_kb_info(kb_info: Dict = None, path: str = None, layout_name="LAYOUT"):
        """
        Creates a Keyboard object from the data in a QMK info.json file.
        Args:
            layout_name: The object in kb_info['layouts'] to use
        """
        if not kb_info:
            with open(path) as f:
                kb_info = json.load(f)
        layout = kb_info["layouts"][layout_name]["layout"]
        keys = [Key(key["x"], key["y"]) for key in layout]

        return Keyboard(keys, kb_info["width"], kb_info["height"])

    def create_layout(self, key_codes: List[str]) -> 'Keyboard':
        """
        Returns a deep copy of this keyboard whose keys have been intialized with the given key codes.
        The provided key codes should be in the same order as the keys used to create this Keyboard.
        """ 
        assert len(key_codes) == len(self.keys), f"There are {len(key_codes)} key_codes but only {len(self.keys)} keys"
        layout = copy.deepcopy(self)
        for key, key_code in zip(layout.keys, key_codes):
            key.code = key_code
        return layout

    def __post_init__(self):
        self.rows = {}
        self.cols = {}
        for key in self.keys:
            # round to the nearest half
            key.col = round(2 * key.x) / 2
            # Intense row stagger is less common and difficult to display as a string,
            # so every row must be a whole number
            key.row = int(key.y)
            if key.row not in self.rows:
                self.rows[key.row] = []
            self.rows[key.row].append(key)
            if key.col not in self.cols:
                self.cols[key.col] = []
            self.cols[key.col].append(key)
