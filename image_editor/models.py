from django.db import models


class Image(models.Model):
    EFFECT_TYPES = (("line_effect", "Line effect"), ("rainbow_effect", "Rainbow effect"),
                    ("palette_rainbow_effect", "Palette rainbow effect"))
    effect_type = models.CharField(max_length=255, choices=EFFECT_TYPES, default="Line effect")
    effect_params = models.CharField(max_length=10 * 1024)
    image = models.ImageField(upload_to="uploaded_images")
