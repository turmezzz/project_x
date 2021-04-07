import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon

from image_editor.image_tools.effects.utils import apply_mask, get_dpi
from .line_effect import LineEffect


class RainbowEffect:
    """
    Example:
    {[
        {
            "background": None,
            "line_width": 20,
            "barrier": 0.5,
            "gaussian_sigma": 5,
            "contour_barrier": 0.01,
            "line_color": "white",
            "line_style": "solid",
            "facecolor": "none"
        }, {
            "background": None,
            "line_width": 20,
            "barrier": 0.5,
            "gaussian_sigma": 10,
            "contour_barrier": 0.01,
            "line_color": "#B16377",
            "line_style": "solid",
            "facecolor": "none"
        }, {
            "background": None,
            "line_width": 20,
            "barrier": 0.5,
            "gaussian_sigma": 15,
            "contour_barrier": 0.01,
            "line_color": "#5285D4",
            "line_style": "solid",
            "facecolor": "none"
        }
    ]}
    """
    base_params_keys = ("lines_params",)

    def check_params_keys(self, params_keys):
        for key in self.base_params_keys:
            if key not in params_keys:
                raise Exception("Wrong line effect params")

    def apply(self, mask, img, params):
        # throws exception if params are wrong
        self.check_params_keys(params.keys())

        prev_img = img
        line_effect = LineEffect()
        for exact_line_params in params["lines_params"]:
            prev_img = line_effect.apply(mask, prev_img, exact_line_params)
        return prev_img



