from qmkformat.parser import parse_layout 

code1 = """
#define SAMPLE code
bool misc = false;

// qmkformat start
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(KC_ESC, KC_1, KC_2, KC_3, KC_4, KC_5, /**/ KC_6, KC_7, KC_8, KC_9, KC_0, KC_NO),
    [1] = LAYOUT(KC_TILD, KC_EXLM, KC_AT, KC_HASH, KC_DLR, KC_PERC, /**/ KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, KC_PGUP, RESET),
};
// qmkformat end

uint16_t add(uint16_t a, uint16_t, b) {
    return a + b;
}
"""

keys1 = [
    ['KC_ESC', 'KC_1', 'KC_2', 'KC_3', 'KC_4', 'KC_5', 'KC_6', 'KC_7', 'KC_8', 'KC_9', 'KC_0', 'KC_NO'],
    ['KC_TILD', 'KC_EXLM', 'KC_AT', 'KC_HASH', 'KC_DLR', 'KC_PERC', 'KC_CIRC', 'KC_AMPR', 'KC_ASTR', 'KC_LPRN', 'KC_RPRN', 'KC_PGUP', 'RESET']
]

def test_parse_layout():
    parsed = parse_layout(code1)
    assert parsed == keys1