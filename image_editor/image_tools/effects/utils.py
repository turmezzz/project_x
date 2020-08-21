import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage.filters import gaussian_filter
from skimage.measure import find_contours


def get_blurred_masks(masks, gaussian_sigma):
    blurred_masks = np.zeros(masks.shape)
    for i in range(masks.shape[2]):
        blurred_masks[..., i] = gaussian_filter(masks[..., i] * 255., sigma=gaussian_sigma) / 255.
    return blurred_masks


def get_contours(masks, gaussian_sigma=5, contour_barier=0.01):
    blurred_masks = get_blurred_masks(masks, gaussian_sigma)
    contours = []
    for i in range(masks.shape[2]):
        contour = np.array(find_contours(blurred_masks[..., i], contour_barier))[0]
        contours.append(contour)
    return np.array(contours)


def apply_mask(image, mask, color, alpha=0.5, barier=0.5):
    for c in range(3):
        image[:, :, c] = np.where(mask >= barier,
                                  image[:, :, c] * (1 - alpha) + alpha * color[c] * 255,
                                  image[:, :, c])
    return image


def get_overall_mask(all_masks):
    common_mask = np.zeros(all_masks.shape[:2])
    for i in range(all_masks.shape[2]):
        common_mask += all_masks[..., i]
    common_mask = np.clip(common_mask, 0., 1.)
    return np.expand_dims(common_mask, axis=2)

def get_dpi ():
    fig0 = plt.figure()
    my_dpi = fig0.dpi
    return my_dpi