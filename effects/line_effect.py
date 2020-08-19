import matplotlib.pyplot as plt
import numpy as np
from effects.utils import apply_mask

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

        #     image_size = 300
        #     dpi = rgb_image.shape[1] * 2.54 / image_size
        #     _, ax = plt.subplots(1, figsize=(rgb_image.shape[0] / dpi ,rgb_image.shape[1] / dpi))
        fig, ax = plt.subplots(1, figsize=(16, 16))
        height, width = img.shape[:2]
        ax.set_ylim(height + 10, -10)
        ax.set_xlim(-10, width + 10)
        ax.axis('off')
        ax.set_title("")

        # Contour
        masked_image = img.astype(np.uint32).copy()
        for verts in contours:
            verts = np.fliplr(verts) - 1
            p = Polygon(verts, facecolor="none", edgecolor='w', lw=line_width, closed=False, ls='-.', snap=False)
            ax.add_patch(p)

        # Background
        if background is not None:
            print(background.shape)
            masked_image = apply_mask(masked_image, background, color=(1, 1, 0), alpha=1.0, barier=barier)

        ax.imshow(masked_image.astype(np.uint8))

        fig.canvas.draw()

        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        return data
