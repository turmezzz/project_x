import os
import sys

import numpy as np

import mrcnn._coco as coco
import mrcnn._model as modellib

MODEL_DIR = "logs"
COCO_MODEL_PATH = "mrcnn/weights/mask_rcnn_coco.h5"

if not os.path.exists(COCO_MODEL_PATH):
    print('error, no weights')
    sys.exit()


class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


class DetectedObject:

    def __init__(self, class_id, score, rois, mask):
        self.class_id = class_id
        self.score = score
        self.rois = rois
        self.mask = mask


class Detector:

    def __init__(self, threshold=0.8):
        self.model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=InferenceConfig())
        self.model.load_weights(COCO_MODEL_PATH, by_name=True)
        self.threshold = threshold

    def detect_image(self, image):
        data = self.model.detect([image], verbose=1)[0]
        human_class_id = 1

        amount = len(data['class_ids'])
        class_ids_list = data['class_ids']
        scores_list = data['scores']
        rois_list = data['rois']
        masks_list = np.array([data['masks'][:, :, i] for i in range(amount)])

        humans = []
        for i in range(amount):
            if class_ids_list[i] == human_class_id and scores_list[i] >= self.threshold:
                obj = DetectedObject(human_class_id, scores_list[i], rois_list[i], masks_list[i])
                humans.append(obj)
        return humans
