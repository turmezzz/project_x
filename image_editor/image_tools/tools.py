import numpy as np


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