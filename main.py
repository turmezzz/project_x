"""
this main.py file is fo testing and debugging
"""

import PIL.Image
import numpy as np
# import matplotlib.pyplot as plt

from image_editor.image_tools.detector import Detector
# from image_editor.image_tools.mrcnn import _visualize
from image_editor.image_tools.image_processor import apply_effect_to_img
from image_editor.image_tools.effects.utils import get_contours, get_blurred_masks, get_overall_mask


def convert_for_visualizer(results):
    amount = len(results)

    if amount == 0:
        return np.empty(0)

    roiss_list = []
    masks_list = np.zeros((results[0].mask.shape[0], results[0].mask.shape[1], amount))
    class_ids_list = []
    scores_list = []
    for i in range(amount):
        roiss_list.append(results[i].rois)
        masks_list[..., i] = results[i].mask
        class_ids_list.append(results[i].class_id)
        scores_list.append(results[i].score)

    return np.array(roiss_list), masks_list, np.array(class_ids_list), np.array(scores_list)


class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

file_path = '/Users/turmezzz/Desktop/ira.png'

raw_image = PIL.Image.open(file_path)
rgb_image = raw_image.convert('RGB')
rgb_image = np.asarray(rgb_image)

detector = Detector(threshold=0.5)
box = convert_for_visualizer(detector.detect_image(rgb_image))

effect_type = 'line_effect'
background = None
line_width = 10
barrier = 0.5
contour_barrier = 0.01
gaussian_sigma = 12
mask = box[1]

params = {'effect_type': effect_type, 'background': background,
          'line_width': line_width, 'barrier': barrier,
          'gaussian_sigma': gaussian_sigma, 'contour_barrier': contour_barrier,}

new_img = apply_effect_to_img(rgb_image, mask, params)

im = PIL.Image.fromarray(new_img)
im.save('/Users/turmezzz/Desktop/new.png')
