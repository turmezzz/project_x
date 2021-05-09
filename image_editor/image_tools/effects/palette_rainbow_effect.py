import matplotlib.pyplot as plt
import numpy as np

from copy import copy
from colorific import palette
from matplotlib.patches import Polygon

from image_editor.image_tools.effects.utils import fill_background, get_dpi, rgb_to_hex
from .line_effect import LineEffect


class PaletteRainbowEffect:
    """
    Example:
        {
            "add_white_lines": True,
            "palette_size": 1,
            "gaussian_sigma_init": 10,
            "gaussian_sigma_step": 10,
            "background": None,
            "line_width": 5,
            "barrier": 0.5,
            "contour_barrier": 0.01,
            "line_style": "solid",
            "facecolor": "none",
        }

    """
    base_params_keys = ("palette_size",)
    optional_params_values = {"gaussian_sigma_init": 10,
                              "gaussian_sigma_step": 10,
                              "contour_barrier": 0.01,
                              "background": None,
                              "line_width": 20,
                              "barrier": 0.5,
                              "facecolor": "none",
                              "line_style": "solid",
                              "add_white_lines": True}

    def check_params_keys(self, params_keys):
        for key in self.base_params_keys:
            if key not in params_keys:
                raise Exception("Wrong line effect params")

    def build_params_for_rainbow(self, raw_params, palette_colors):
        line_params = {
            "background": None,
            "line_width": 20,
            "barrier": 0.5,
            "contour_barrier": 0.01,
            "line_style": "solid",
            "facecolor": "none",
        }
        raw_params["palette_size"] = min(raw_params["palette_size"], len(palette_colors))

        gaussian_sigma_init = raw_params["gaussian_sigma_init"] if "gaussian_sigma_init" in raw_params else self.optional_params_values["gaussian_sigma_init"]
        gaussian_sigma_step = raw_params["gaussian_sigma_step"] if "gaussian_sigma_step" in raw_params else self.optional_params_values["gaussian_sigma_step"]

        params = []
        for i in range(raw_params["palette_size"]):
            params.append(copy(line_params))
            params[-1]["line_color"] = palette_colors[i]
            params[-1]["gaussian_sigma"] = gaussian_sigma_init + i * gaussian_sigma_step
            params[-1]["line_width"] = raw_params["line_width"]
        return params

    def apply(self, mask, img, params):
        print(params)

        # throws exception if params are wrong
        self.check_params_keys(params.keys())

        # base params
        palette_size = params["palette_size"]

        # optional params
        add_white_lines = params["add_white_lines"] if "add_white_lines" in params else self.optional_params_values["add_white_lines"]

        palette_colors = []
        white = "#FFFFFF"
        if add_white_lines:
            params["palette_size"] += 1
            palette_colors.append(white)
        for color in palette.extract_colors(img, max_colors=palette_size).colors:
            palette_colors.append(rgb_to_hex(color.value))

            palette_colors.append(white)
            params["palette_size"] += 1

        prev_img = img
        line_effect = LineEffect()
        lines_params = self.build_params_for_rainbow(params, palette_colors)
        for exact_line_params in lines_params:
            prev_img = line_effect.apply(mask, prev_img, exact_line_params)
        return prev_img
