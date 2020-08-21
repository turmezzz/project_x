"""
this main.py file is fo testing and debugging
"""

import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

from detector import Detector
from mrcnn import _visualize
from image_processor import apply_effect_to_img
from effects.utils import get_contours, get_blurred_masks, get_overall_mask


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

contour_barier = 0.01
contours = get_contours(box[1], gaussian_sigma=12, contour_barier=contour_barier)  # contours[i] = [y, x]

params = {'contours': contours, 'background': None, 'line_width': 10, 'barier': 0.5}

new_img = apply_effect_to_img(rgb_image, 'line_effect', params)

im = PIL.Image.fromarray(new_img)
im.save('/Users/turmezzz/Desktop/new.png')


# box = convert_for_visualizer(detector.detect_image(rgb_image))
# if len(box) != 0:
#     _visualize.display_instances(rgb_image,
#                                  box[0],
#                                  box[1],
#                                  box[2],
#                                  class_names,
#                                  box[3])
