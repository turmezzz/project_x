import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon

from image_editor.image_tools.effects.utils import apply_mask, get_dpi
from .utils import get_contours


class LineEffect:
    """
    Example:
        {"background": None,
        "line_width": 10,
        "barrier": 0.5,
        "gaussian_sigma": 10,
        "contour_barrier": 0.01,
        "line_color": "white",
        "line_style": "solid",
        "facecolor": "none"}
    """
    base_params_keys = tuple()
    optional_params_values = {"gaussian_sigma": 10,
                              "contour_barrier": 0.01,
                              "background": None,
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

        # optional params
        gaussian_sigma = params["gaussian_sigma"] if "gaussian_sigma" in params else self.optional_params_values[
            "gaussian_sigma"]
        contour_barrier = params["contour_barrier"] if "contour_barrier" in params else self.optional_params_values[
            "contour_barrier"]
        background = params["background"] if "background" in params else self.optional_params_values["background"]
        line_width = params["line_width"] if "line_width" in params else self.optional_params_values["line_width"]
        barrier = params["barrier"] if "barrier" in params else self.optional_params_values["barrier"]
        facecolor = params["facecolor"] if "facecolor" in params else self.optional_params_values["facecolor"]
        line_color = params["line_color"] if "line_color" in params else self.optional_params_values["line_color"]
        line_style = params["line_style"] if "line_style" in params else self.optional_params_values["line_style"]

        my_dpi = get_dpi()
        fig, ax = plt.subplots(1, figsize=(img.shape[1] / my_dpi, img.shape[0] / my_dpi), dpi=my_dpi)
        ax.axis("off")

        # Contour
        contours = get_contours(mask, gaussian_sigma=gaussian_sigma, contour_barrier=contour_barrier)
        masked_image = img.astype(np.uint32).copy()
        for verts in contours:
            verts = np.fliplr(verts) - 1  # verts = [x, y]
            p = Polygon(verts, facecolor=facecolor, edgecolor=line_color, lw=line_width, closed=False, ls=line_style,
                        snap=False)
            ax.add_patch(p)

        # Background
        if background is not None:
            masked_image = apply_mask(masked_image, background, color=(1, 1, 0), alpha=1.0, barrier=barrier)
        ax.imshow(masked_image.astype(np.uint8), aspect="auto")
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        s, (width, height) = fig.canvas.print_to_buffer()

        data = np.frombuffer(s, np.uint8).reshape((height, width, 4))
        return data
