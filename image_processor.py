from effects.line_effect import LineEffect

titles_2_effect = {'line_effect': LineEffect}


def apply_effect_to_img(img, effect_title, params):
    if effect_title in titles_2_effect:
        effect = titles_2_effect[effect_title]()
        effect.apply(img, params)
