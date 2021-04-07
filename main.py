"""
this main.py file is fo testing and debugging
"""

import PIL.Image
import numpy as np

from image_editor.image_tools.detector import Detector
from image_editor.image_tools.image_processor import apply_effect_to_img
from image_editor.image_tools.effects.utils import get_contours, get_blurred_masks, get_overall_mask
from image_editor.image_tools.tools import convert_for_visualizer


class_names = ["BG", "person", "bicycle", "car", "motorcycle", "airplane",
               "bus", "train", "truck", "boat", "traffic light",
               "fire hydrant", "stop sign", "parking meter", "bench", "bird",
               "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
               "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie",
               "suitcase", "frisbee", "skis", "snowboard", "sports ball",
               "kite", "baseball bat", "baseball glove", "skateboard",
               "surfboard", "tennis racket", "bottle", "wine glass", "cup",
               "fork", "knife", "spoon", "bowl", "banana", "apple",
               "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
               "donut", "cake", "chair", "couch", "potted plant", "bed",
               "dining table", "toilet", "tv", "laptop", "mouse", "remote",
               "keyboard", "cell phone", "microwave", "oven", "toaster",
               "sink", "refrigerator", "book", "clock", "vase", "scissors",
               "teddy bear", "hair drier", "toothbrush"]

file_path = "/Users/turmetsmakoev/Desktop/n00.png"

raw_image = PIL.Image.open(file_path)
rgb_image = raw_image.convert("RGB")
rgb_image = np.asarray(rgb_image)

detector = Detector(threshold=0.5)
detection_result = convert_for_visualizer(detector.detect_image(rgb_image))

# effect_type = "line_effect"
# background = None
# line_width = 10
# barrier = 0.5
# contour_barrier = 0.01
# gaussian_sigma = 12


params = {
            "effect_type": "palette_rainbow_effect",
            "add_white_lines": True,
            "palette_size": 3,
            "gaussian_sigma_init": 20,
            "gaussian_sigma_step": 10,
            "background": None,
            "line_width": 20,
            "barrier": 0.5,
            "contour_barrier": 0.01,
            "line_style": "solid",
            "facecolor": "none",
        }

# params = {
#     "effect_type": "line_effect",
#     "background": None,
#     "line_width": 10,
#     "barrier": 0.5,
#     "gaussian_sigma": 10,
#     "contour_barrier": 0.01,
#     "line_color": "white",
#     "line_style": "solid",
#     "facecolor": "none"
# }


new_img = apply_effect_to_img(rgb_image, detection_result, params)

im = PIL.Image.fromarray(new_img)
im.save("/Users/turmetsmakoev/Desktop/out.png")
