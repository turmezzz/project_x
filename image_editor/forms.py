from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("effect_type", "effect_params", "image")

        placeholder = {'background': None, 'line_width': 10, 'barrier': 0.5, 'gaussian_sigma': 12,
                       'contour_barrier': 0.01}
        widgets = {
            "effect_params": forms.Textarea(attrs={"placeholder": str(placeholder)}),
        }
