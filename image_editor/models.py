from django.db import models


class LineEffect(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    line_color = models.CharField(default="#ffffff", max_length=7)


class BackgroundFillingEffect(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    line_color = models.CharField(default="#ffffff", max_length=7)
    background_color = models.CharField(default="#000000", max_length=7)


