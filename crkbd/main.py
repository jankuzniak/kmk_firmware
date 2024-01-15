print("Starting CRKBD")
import board

from kb import KMKKeyboard

from kmk.extensions.rgb import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.peg_oled_display import (
    Oled,
    OledDisplayMode,
    OledReactionType,
    OledData,
)
from kmk.modules.combos import Combos, Chord, Sequence

keyboard = KMKKeyboard()

# Adding extensions
rgb = RGB(
    pixel_pin=keyboard.rgb_pixel_pin,
    num_pixels=27,
    val_limit=100,
    hue_default=81,
    sat_default=120,
    val_default=40,
    animation_mode=AnimationModes.STATIC,
)
keyboard.modules.append(rgb)

# TODO Comment one of these on each side
# split_side = SplitSide.RIGHT
split = Split(
    split_side=SplitSide.LEFT,
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=None,  # Second uart pin to allow 2 way communication
    use_pio=False,  # allows for UART to be used with PIO
)
keyboard.extensions.append(split)

oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["layer"]},
        corner_two={0: OledReactionType.LAYER, 1: ["1", "2", "3", "4"]},
        corner_three={
            0: OledReactionType.LAYER,
            1: ["base", "raise", "lower", "adjust"],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: ["qwerty", "nums", "shifted", "leds"],
        }, 
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

combos = Combos()
combos.combos = [
    Chord((KC.Q, KC.W), KC.LGUI),
]
keyboard.modules.append(combos)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

L_NAVI    = KC.MO(1)
L_SYMBOLS = KC.MO(2)

# RGB_TOG = KC.RGB_TOG
# RGB_HUI = KC.RGB_HUI
# RGB_HUD = KC.RGB_HUI
# RGB_SAI = KC.RGB_SAI
# RGB_SAD = KC.RGB_SAD
# RGB_VAI = KC.RGB_VAI
# RGB_VAD = KC.RGB_VAD

combo_layers = {
  (1, 2): 3,
   }
keyboard.modules.append(Layers(combo_layers))

# fmt: off
keyboard.keymap = [
    [  # QWERTY
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        KC.LSFT,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LCTL,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LALT,   KC.SPACE,  L_NAVI,     L_SYMBOLS,   KC.BACKSPACE,  KC.RALT,
    ],
    [  # NAVIGATION
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
    [  # SYMBOLS
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
    [  # NUMPAD
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
    [  # NUMBERS
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
    [  # SWITCH
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
    [  # MEDIA
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
        _______,  _______,  _______,  _______,  _______,  _______,                         _______,  _______,  _______,  _______,  _______,  _______,\
                                                _______,  _______,  _______,     _______,  _______,  _______,
    ],
]

# keyboard.keymap = [
#     [  #QWERTY
#         KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
#         KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
#         KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
#                                             KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
#     ],
#     [  #LOWER
#         KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
#         KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
#         KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
#                                             KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
#     ],
#     [  #RAISE
#         KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
#         KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\
#         KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
#                                             KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
#     ],
#     [  #ADJUST
#         RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
#         XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
#         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
#                                             KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
#     ]
# ]

if __name__ == "__main__":
    keyboard.go()
