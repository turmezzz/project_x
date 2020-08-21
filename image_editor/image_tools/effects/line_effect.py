import matplotlib.pyplot as plt
import numpy as np
from effects.utils import apply_mask
from effects.utils import get_dpi

from matplotlib.patches import Polygon


class LineEffect:
    base_params_keys = ('contours', 'background', 'line_width', 'barier')

    def check_params_keys(self, params_keys):
        for key in self.base_params_keys:
            if key not in params_keys:
                raise Exception('Wrong line effect params')

    def apply(self, img, params):
        # throws exception if params are wrong
        self.check_params_keys(params.keys())

        contours = params['contours']
        background = params['background']
        line_width = params['line_width']
        barier = params['barier']

        my_dpi = get_dpi()
        fig, ax = plt.subplots(1, figsize=(img.shape[1] / my_dpi, img.shape[0] / my_dpi), dpi=my_dpi)
        ax.axis('off')

        # Contour
        masked_image = img.astype(np.uint32).copy()
        for verts in contours:
            verts = np.fliplr(verts) - 1  # verts = [x, y]
            p = Polygon(verts, facecolor="none", edgecolor='w', lw=line_width, closed=False, ls='-', snap=False)
            ax.add_patch(p)

        # Background
        if background is not None:
            masked_image = apply_mask(masked_image, background, color=(1, 1, 0), alpha=1.0, barier=barier)
        ax.imshow(masked_image.astype(np.uint8), aspect='auto')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        s, (width, height) = fig.canvas.print_to_buffer()

        data = np.frombuffer(s, np.uint8).reshape((height, width, 4))
        return data
