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

        line_effect = LineEffect()
        return line_effect.apply(mask, img, params)
