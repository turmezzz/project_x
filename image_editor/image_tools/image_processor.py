from .effects.line_effect import LineEffect
from .effects.utils import get_contours

effect_type_2_effect = {'line_effect': LineEffect}


def apply_effect_to_img(img, mask, params):
    effect_type = params['effect_type']
    if effect_type in effect_type_2_effect:
        gaussian_sigma = params['gaussian_sigma']
        contour_barrier = params['contour_barrier']
        contours = get_contours(mask, gaussian_sigma=gaussian_sigma, contour_barrier=contour_barrier)
        params['contours'] = contours
        effect = effect_type_2_effect[effect_type]()
        return effect.apply(img, params)
