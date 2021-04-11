
// qmkformat start
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {                                                                                               //
    [0] = LAYOUT(                                                                                                                                            //
        KC_ESC, KC_1, KC_2, KC_3, KC_4, KC_5, /**/ KC_6, KC_7, KC_8, KC_9, KC_0, KC_NO,                                                                      //
        KC_NO, KC_Q, KC_W, KC_E, KC_R, KC_T, /**/ KC_Y, KC_U, KC_I, KC_O, KC_P, KC_BSPC,                                                                     //
        KC_TAB, LCTL_T(KC_A), LGUI_T(KC_S), LALT_T(KC_D), LSFT_T(KC_F), KC_G, /**/ KC_H, KC_J, KC_K, KC_L, RCTL_T(KC_SCLN), KC_QUOT,                         //
        KC_LSFT, C_S_T(KC_Z), SGUI_T(KC_X), HAS(KC_C), LT(3, KC_V), KC_B, KC_GRV, /**/ KC_DEL, KC_N, KC_M, KC_COMM, RGUI_T(KC_DOT), C_S_T(KC_SLSH), KC_RSFT, //
        /*                                            */ KC_ESC, KC_SPC, MO(1), /**/ KC_RSFT, MO(2), KC_PENT),
    [1] = LAYOUT(
        //
        KC_TILD, KC_EXLM, KC_AT, KC_HASH, KC_DLR, KC_PERC, /**/ KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, KC_PGUP, RESET, KC_1, KC_2, KC_3, KC_4, KC_5, KC_6, KC_7, KC_8, KC_9, KC_NO, KC_PGDN, KC_DEL, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_LBRC, KC_RBRC, KC_4, KC_5, KC_6, KC_0, KC_HOME, BL_STEP, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_LCBR, KC_LPRN, KC_RPRN, KC_RCBR, KC_1, KC_2, KC_3, KC_NO, KC_END, KC_TRNS, KC_TRNS, KC_DEL, KC_DEL, KC_TRNS, KC_P0),
    [2] = LAYOUT(KC_F12, KC_F1, KC_F2, KC_F3, KC_F4, KC_F5, KC_F6, KC_F7, KC_F8, KC_F9, KC_F10, KC_F11, RGB_TOG,                            //
                 KC_EXLM, KC_AT, KC_HASH, KC_DLR, KC_PERC, KC_CIRC, /**/ KC_AMPR, KC_ASTR, KC_TILD, KC_NO, KC_TRNS, RGB_MOD,                //
                 KC_LBRC, KC_RBRC, KC_UNDS, KC_LCBR, KC_RCBR, /**/ KC_GRV, KC_EQL, KC_MINS, KC_LPRN, KC_RPRN, KC_DQUO,                      //
                 KC_MUTE, KC_PIPE, KC_BSLS, KC_COLN, KC_BSPC, KC_NO, /**/ KC_LPRN, KC_TRNS, KC_NO, KC_PLUS, KC_LT, KC_GT, KC_SLSH, KC_TRNS, //
                 KC_TRNS, KC_NO, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS),
    [3] = LAYOUT(KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_MENU, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_LEFT, KC_DOWN, KC_UP, KC_RGHT, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS)};
// qmkformat end

uint16_t add(uint16_t a, uint16_t, b)
{
    return a + b;
}
