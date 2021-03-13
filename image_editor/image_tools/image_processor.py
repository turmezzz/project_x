from .effects.line_effect import LineEffect
from .effects.rainbow_effect import RainbowEffect
from .effects.palette_rainbow_effect import PaletteRainbowEffect

effect_type_2_effect = {"line_effect": LineEffect, "rainbow_effect": RainbowEffect,
                        "palette_rainbow_effect": PaletteRainbowEffect}


def apply_effect_to_img(img, mask, params):
    effect_type = params["effect_type"]
    if effect_type in effect_type_2_effect:
        effect = effect_type_2_effect[effect_type]()
        return effect.apply(mask, img, params)
