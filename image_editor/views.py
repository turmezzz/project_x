from django.shortcuts import render
from project_x_web.settings import BASE_DIR
from .forms import ImageForm

import PIL.Image
import numpy as np
import os
import pickle

from image_editor.image_tools.detector import Detector
from image_editor.image_tools.image_processor import apply_effect_to_img
from image_editor.image_tools.tools import convert_for_visualizer


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            upload_image_path = form.instance.image.url
            effect_type = form.instance.effect_type
            effect_params = eval(form.instance.effect_params)
            effect_params["effect_type"] = effect_type
            print(effect_params)

            path = BASE_DIR + upload_image_path
            print(os.path.abspath(__file__))
            print(path)

            raw_image = PIL.Image.open(path)
            rgb_image = raw_image.convert("RGB")
            rgb_image = np.asarray(rgb_image)
            print("have rgb_image")

            mock = False
            if mock:
                with open("mock.pickle", "rb") as f:
                    mask = convert_for_visualizer(pickle.load(f))[1]
                    print("mock loaded")
            else:
                detector = Detector()
                mask = convert_for_visualizer(detector.detect_image(rgb_image))[1]
                print(len(mask))
            print("have mask")

            new_img = apply_effect_to_img(rgb_image, mask, effect_params)
            print("have applied effect")

            processed_image_path = "/Users/turmetsmakoev/Desktop/project_x_web/media/processed_images/out.png"
            im = PIL.Image.fromarray(new_img)
            im.save(processed_image_path)
            print("have processed image")

            return render(request, "home.html", {"form": form, "image_path": "/media/processed_images/out.png"})
    else:
        form = ImageForm()
    return render(request, "home.html", {"form": form})
