from django.db import models


class LineEffect(models.Model):
    image = models.ImageField(upload_to="uploaded_images")
    line_width = models.IntegerField()
    line_indent = models.IntegerField()
    line_color = models.CharField(default="#c8c8c8", max_length=7)
