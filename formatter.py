from icecream import ic
import re
from typing import List


def get_lines(path: str):
    with open(path) as f:
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
        layout_keys.append(
            [re.search("[\w\(\)]+", key).group(0) for key in layout_str.split(",")]
        )
    return layout_keys


def parse_layout(lines: str):
    lines = get_keymap(lines)
    lines = remove_excess_white_space(lines)
    layout_strs = get_layouts_strs(lines)
    return get_layout_keys(layout_strs)


rows = [12, 12, 14, 6]

lines = get_lines("old.c")
layout_keys = parse_layout(lines)

