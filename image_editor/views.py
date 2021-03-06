from django.shortcuts import render
from project_x_web.settings import BASE_DIR
from .forms import LineEffectForm, BackgroundFillingEffectForm, NeonLineEffectForm, PaletteRainbowEffectForm

import PIL.Image
import numpy as np
import random

from image_editor.image_tools.detector import Detector
from image_editor.image_tools.image_processor import apply_effect_to_img
from image_editor.image_tools.tools import convert_for_visualizer


def process_image(upload_image_path, effect_params):
    file_path = BASE_DIR + upload_image_path

    raw_image = PIL.Image.open(file_path)
    rgb_image = raw_image.convert("RGB")
    rgb_image = np.asarray(rgb_image)

    detector = Detector()
    detection_result = convert_for_visualizer(detector.detect_image(rgb_image))

    new_img = apply_effect_to_img(rgb_image, detection_result, effect_params)

    processed_image_path = "/media/processed_images/out_" + str(random.randint(1000, 9999)) + ".png"
    im = PIL.Image.fromarray(new_img)
    im.save(BASE_DIR + processed_image_path)

    return processed_image_path


def line_effect(request):
    if request.method == "POST":
        form = LineEffectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            upload_image_path = form.instance.image.url
            line_width = form.instance.line_width
            line_indent = form.instance.line_indent
            line_color = form.instance.line_color
            effect_params = {
                "effect_type": "line_effect",
                "line_width": line_width,
                "gaussian_sigma": line_indent,
                "line_color": line_color,
            }

            processed_image_path = process_image(upload_image_path, effect_params)

            return render(request, "line_effect.html", {"form": form, "image_path": processed_image_path})
    else:
        form = LineEffectForm()
    return render(request, "line_effect.html", {"form": form})


def background_filling_effect(request):
    if request.method == "POST":
        form = BackgroundFillingEffectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            upload_image_path = form.instance.image.url
            line_width = form.instance.line_width
            line_indent = form.instance.line_indent
            line_color = form.instance.line_color
            background_color = form.instance.background_color
            apply_bw_filter = form.instance.apply_bw_filter
            effect_params = {
                "effect_type": "background_filling_effect",
                "line_width": line_width,
                "gaussian_sigma": 1,
                "line_color": line_color,
                "background_color": background_color,
                "mask_conv_kernel_size": 2 * line_indent + 1,
                "apply_bw_filter_to_inline": apply_bw_filter
            }

            processed_image_path = process_image(upload_image_path, effect_params)

            return render(request, "background_filling_effect.html", {"form": form, "image_path": processed_image_path})
    else:
        form = BackgroundFillingEffectForm()
    return render(request, "background_filling_effect.html", {"form": form})


def neon_line_effect(request):
    if request.method == "POST":
        form = NeonLineEffectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            upload_image_path = form.instance.image.url
            line_width = form.instance.line_width
            line_indent = form.instance.line_indent
            line_color = form.instance.line_color
            neon_rate = form.instance.neon_rate
            effect_params = {
                "effect_type": "neon_line_effect",
                "line_width": line_width,
                "gaussian_sigma": line_indent,
                "line_color": line_color,
                "neon_rate": neon_rate,
            }

            processed_image_path = process_image(upload_image_path, effect_params)

            return render(request, "neon_line_effect.html", {"form": form, "image_path": processed_image_path})
    else:
        form = NeonLineEffectForm()
    return render(request, "neon_line_effect.html", {"form": form})


def palette_rainbow_effect(request):
    if request.method == "POST":
        form = PaletteRainbowEffectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            upload_image_path = form.instance.image.url
            line_width = form.instance.line_width
            line_indent = form.instance.line_indent
            palette_size = form.instance.palette_size
            effect_params = {
                "effect_type": "palette_rainbow_effect",
                "line_width": line_width,
                "gaussian_sigma_init": line_indent,
                "gaussian_sigma_step": line_indent,
                "palette_size": palette_size,
            }

            processed_image_path = process_image(upload_image_path, effect_params)

            return render(request, "palette_rainbow_effect.html", {"form": form, "image_path": processed_image_path})
    else:
        form = PaletteRainbowEffectForm()
    return render(request, "palette_rainbow_effect.html", {"form": form})