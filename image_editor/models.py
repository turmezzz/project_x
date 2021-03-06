from django.db import models


class Image(models.Model):
    EFFECT_TYPES = (("line_effect", "Line effect"),)
    effect_type = models.CharField(max_length=255, choices=EFFECT_TYPES, default="Line effect")
    effect_params = models.CharField(max_length=255)
    image = models.ImageField(upload_to="uploaded_images")
