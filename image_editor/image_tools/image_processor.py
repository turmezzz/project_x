import numpy as np

from .effects.line_effect import LineEffect
from .effects.rainbow_effect import RainbowEffect
from .effects.palette_rainbow_effect import PaletteRainbowEffect

effect_type_2_effect = {"line_effect": LineEffect, "rainbow_effect": RainbowEffect,
                        "palette_rainbow_effect": PaletteRainbowEffect}


def calculate_object_square(image_shape, bounding_box):
    image_square = image_shape[0] * image_shape[1]
    left_top_y, left_top_x, right_bottom_y, right_bottom_x = bounding_box
    return (right_bottom_y - left_top_y) * (right_bottom_x - left_top_x) / image_square


def apply_effect_to_img(img, detection_result, params):
    bounding_boxes = detection_result[0]
    all_masks = detection_result[1]

    detections_amount = len(bounding_boxes)
    if detections_amount == 0:
        return None

    squares = [(calculate_object_square(img.shape, box), i) for i, box in enumerate(bounding_boxes)]
    squares.sort(key=lambda x: x[1])
    good_masks_ids = []
    max_square = 0
    square_difference_coef = 4
    for square, i in squares:
        if i == 0:
            good_masks_ids.append(i)
            max_square = square
        elif square >= max_square / square_difference_coef:
            good_masks_ids.append(i)

    good_masks = []
    for i in good_masks_ids:
        good_masks.append(all_masks[::, ::, i])
    good_masks = np.dstack(good_masks)

    effect_type = params["effect_type"]
    if effect_type in effect_type_2_effect:
        effect = effect_type_2_effect[effect_type]()
        return effect.apply(good_masks, img, params)
