import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon

from image_editor.image_tools.effects.utils import fill_background, get_dpi
from .utils import get_contours


def get_alpha(neon_batches, neon_iteration):
    return 1 / neon_batches


class NeonLineEffect:
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
                              "background_color": None,
                              "line_width": 10,
                              "barrier": 0.5,
                              "facecolor": "none",
                              "line_color": "white",
                              "line_style": "solid"}

    def check_params_keys(self, params_keys):
        for key in self.base_params_keys:
            if key not in params_keys:
                raise Exception("Wrong line effect params")

    def apply(self, masks, img, params):
        # throws exception if params are wrong
        self.check_params_keys(params.keys())

        # optional params
        gaussian_sigma = params["gaussian_sigma"] if "gaussian_sigma" in params else self.optional_params_values[
            "gaussian_sigma"]
        contour_barrier = params["contour_barrier"] if "contour_barrier" in params else self.optional_params_values[
            "contour_barrier"]
        background_color = params["background_color"] if "background_color" in params else self.optional_params_values["background_color"]
        line_width = params["line_width"] if "line_width" in params else self.optional_params_values["line_width"]
        barrier = params["barrier"] if "barrier" in params else self.optional_params_values["barrier"]
        facecolor = params["facecolor"] if "facecolor" in params else self.optional_params_values["facecolor"]
        line_color = params["line_color"] if "line_color" in params else self.optional_params_values["line_color"]
        line_style = params["line_style"] if "line_style" in params else self.optional_params_values["line_style"]

        my_dpi = get_dpi()
        fig, ax = plt.subplots(1, figsize=(img.shape[1] / my_dpi, img.shape[0] / my_dpi), dpi=my_dpi)
        ax.axis("off")

        # Contour
        contours = get_contours(masks, gaussian_sigma=gaussian_sigma, contour_barrier=contour_barrier)

        neon_batches = params["neon_batches"]

        for verts in contours:
            verts = np.fliplr(verts) - 1  # verts = [x, y]
            for neon_iteration in range(neon_batches):

                local_alpha, local_line_width = get_alpha(neon_batches, neon_iteration), (line_width / neon_batches) * (neon_iteration + 1)

                p = Polygon(verts,
                            facecolor=facecolor,
                            edgecolor=line_color,
                            linewidth=local_line_width,
                            closed=False,
                            ls=line_style,
                            snap=False,
                            alpha=local_alpha)
                ax.add_patch(p)
            color_line_width = line_width * 0.05
            p = Polygon(verts,
                        facecolor=facecolor,
                        edgecolor=line_color,
                        linewidth=color_line_width,
                        closed=False,
                        ls=line_style,
                        snap=False,
                        alpha=1)
            ax.add_patch(p)
            white_line_width = line_width * 0.02
            white_alpha = 0.9
            p = Polygon(verts,
                        facecolor=facecolor,
                        edgecolor="white",
                        linewidth=white_line_width,
                        closed=False,
                        ls=line_style,
                        snap=False,
                        alpha=white_alpha)
            ax.add_patch(p)

        # Background
        img = img.astype(np.uint32).copy()
        if background_color is not None:
            img = fill_background(img, masks, color=background_color, alpha=1.0, barrier=barrier)

        ax.imshow(img.astype(np.uint8), aspect="auto")
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        s, (width, height) = fig.canvas.print_to_buffer()

        data = np.frombuffer(s, np.uint8).reshape((height, width, 4))
        return data
