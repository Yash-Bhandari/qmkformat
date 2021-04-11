from qmkformat.keyboard import Keyboard
from qmkformat.parser import read_and_parse_layout
from qmkformat.formatter import StringFormatter

layouts = read_and_parse_layout("cfiles/old.c")
iris = Keyboard.from_kb_info(path="keyboards/iris_rev4.json")
StringFormatter(layouts, iris)
