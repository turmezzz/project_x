from django.db import models


class LineEffectModel(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    line_color = models.CharField(default="#ffffff", max_length=7)


class BackgroundFillingEffectModel(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    line_color = models.CharField(default="#ffffff", max_length=7)
    background_color = models.CharField(default="#000000", max_length=7)
    apply_bw_filter = models.BooleanField(default=False)


class NeonLineEffectModel(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    neon_rate = models.IntegerField()
    line_color = models.CharField(default="#ffffff", max_length=7)


class PaletteRainbowEffectModel(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    palette_size = models.IntegerField()
