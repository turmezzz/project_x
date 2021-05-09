from django import forms
from .models import LineEffect


class LineEffectForm(forms.ModelForm):
    class Meta:
        model = LineEffect
        fields = ("image", "line_width", "line_indent", "line_color")

        image_attrs = {"class": "form-control",
                       "type": "file",
                       "id": "image",
                       "accept": ".png, .jpg, .jpeg",
                       "onchange": "loadFile(event)"}

        line_width_attrs = {"type": "range",
                            "class": "form-control-range",
                            "id": "lineWidth",
                            "min": "1",
                            "max": "100",
                            "value": "50"}

        line_indent_attrs = {"type": "range",
                             "class": "form-control-range",
                             "id": "lineIndent",
                             "min": "1",
                             "max": "100",
                             "value": "10"}

        line_color_attrs = {"type": "color",
                            "class": "form-control form-control-color",
                            "id": "exampleColorInput",
                            "value": "#c8c8c8",
                            "title": "Choose your color"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs)
        }
