import sys
import re
from typing import List


def get_lines(path: str):
    try:
        with open(path) as f:
            return "".join(f.readlines())
    except UnicodeDecodeError:
        with open(path, encoding='utf8') as f:
            return "".join(f.readlines())



def get_keymap(lines: str):
    """Extracts the part of the code that contains the keymap matrices"""
    parsed = [line for line in lines.split("\n") if line]

    start = end = 0
    for i, line in enumerate(parsed):
        if "qmkformat start" in line:
            start = i + 1
        if "qmkformat end" in line:
            end = i
            break

    layout = "".join(parsed[start:end])
    return layout[layout.find("{") + 1 : layout.find("}")]


def remove_excess_white_space(lines: str):
    """For readability during dev/debugging"""
    two_plus_white_space = r"\s{2,}"
    return re.sub(two_plus_white_space, "", lines)


def get_layouts_strs(lines: str) -> List[str]:
    # LAYOUT(part we want) misc [ or end of string
    # https://stackoverflow.com/questions/12083308/in-regex-match-either-the-end-of-the-string-or-a-specific-character
    inside_layout = r"LAYOUT\(([^\[]+)\).*?(\[|$)"
    # the [ or end of string part has to be matchd with a capture group
    # that's why we only care about the first match, which is the actual layout
    return [match[0] for match in re.findall(inside_layout, lines)]


def get_layout_keys(layout_strs: List[str]) -> List[List[str]]:
    layout_keys = []
    for layout_str in layout_strs:
        keys = [re.search(r"[\w\(\)]+", key).group(0) for key in layout_str.split(",")]

        # the regex above will break up a keycode like 'MO(ALT,2)' into 'MO(ALT' and '2)',
        # so now we glue those keycodes back together
        merged_keys = merge_split_consecutive_keycodes(keys)
        layout_keys.append(merged_keys)
    return layout_keys

def merge_split_consecutive_keycodes(keys: List[str]):
    incomplete_keycode=''
    merged_keys = []
    for key in keys:
        if incomplete_keycode:
            key = f'{incomplete_keycode},{key}'
            incomplete_keycode = ''
        if key.count('(') == key.count(')'):
            merged_keys.append(key)
        else:
            incomplete_keycode = key 
    return merged_keys




def parse_layout(keymap_c: str):
    """
    Parses C code from a keymap.c file into a 2d list with the keys in each layer.
    """
    lines = get_keymap(keymap_c)
    lines = remove_excess_white_space(lines)
    layout_strs = get_layouts_strs(lines)
    return get_layout_keys(layout_strs)


def read_and_parse_layout(path: str):
    lines = get_lines(path)
    return parse_layout(lines)

if __name__ == '__main__':
    path = sys.argv[1]
    parsed = read_and_parse_layout(path)
    for i, layout in enumerate(parsed):
        print("Layer #:", i)
        print('-'*40)
        print(layout)
        print('-'*40)
