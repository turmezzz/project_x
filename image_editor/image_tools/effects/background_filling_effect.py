import matplotlib.pyplot as plt
import numpy as np

from copy import copy
from colorific import palette
from matplotlib.patches import Polygon

from image_editor.image_tools.effects.utils import fill_background, get_dpi, rgb_to_hex
from .line_effect import LineEffect


class BackgroundFillingEffect:
    """
    Example:
        {
            "background_color": "white",
            "apply_bw_filter": "True",
            "line_width": 10,
            "barrier": 0.5,
            "gaussian_sigma": 10,
            "contour_barrier": 0.01,
            "line_color": "white",
            "line_style": "solid",
            "facecolor": "none"
        }
    """
    base_params_keys = tuple()
    optional_params_values = {"gaussian_sigma": 10,
                              "contour_barrier": 0.01,
                              "line_width": 10,
                              "barrier": 0.5,
                              "facecolor": "none",
                              "line_color": "white",
                              "line_style": "solid"}

    def check_params_keys(self, params_keys):
        for key in self.base_params_keys:
            if key not in params_keys:
                raise Exception("Wrong line effect params")

    def apply(self, mask, img, params):
        # throws exception if params are wrong
        self.check_params_keys(params.keys())

        if params["apply_bw_filter_to_inline"] or params["apply_bw_filter_to_outline"]:
            inline = params["apply_bw_filter_to_inline"]
            outline = params["apply_bw_filter_to_outline"]
            bw_img = img.copy()
            h, w, d = mask.shape
            for j in range(h):
                for i in range(w):
                    in_mask = False
                    for k in range(d):
                        if mask[j, i, k] == 1:
                            in_mask = True
                            if inline:
                                box = sum(bw_img[j, i]) / 3
                                bw_img[j, i] = (box, box, box)
                    if outline and not in_mask:
                        box = sum(bw_img[j, i]) / 3
                        bw_img[j, i] = (box, box, box)
        else:
            bw_img = img

        line_effect = LineEffect()
        return line_effect.apply(mask, bw_img, params)
