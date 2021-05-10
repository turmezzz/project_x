from django import forms
from .models import LineEffect, BackgroundFillingEffect


LINE_WIDTH_MIN = 1
LINE_WIDTH_MAX = 300

LINE_INDENT_MIN = 10
LINE_INDENT_MAX = 100


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
                            "min": LINE_WIDTH_MIN,
                            "max": LINE_WIDTH_MAX,
                            "value": 20}

        line_indent_attrs = {"type": "range",
                             "class": "form-control-range",
                             "id": "lineIndent",
                             "min": LINE_INDENT_MIN,
                             "max": LINE_INDENT_MAX,
                             "value": 20}

        line_color_attrs = {"type": "color",
                            "class": "form-control form-control-color",
                            "id": "exampleColorInput"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs)
        }


class BackgroundFillingEffectForm(forms.ModelForm):
    class Meta:
        model = BackgroundFillingEffect
        fields = ("image", "line_width", "line_indent", "line_color", "background_color")

        image_attrs = {"class": "form-control",
                       "type": "file",
                       "id": "image",
                       "accept": ".png, .jpg, .jpeg",
                       "onchange": "loadFile(event)"}

        line_width_attrs = {"type": "range",
                            "class": "form-control-range",
                            "id": "lineWidth",
                            "min": LINE_WIDTH_MIN,
                            "max": LINE_WIDTH_MAX,
                            "value": 20}

        line_indent_attrs = {"type": "range",
                             "class": "form-control-range",
                             "id": "lineIndent",
                             "min": LINE_INDENT_MIN,
                             "max": LINE_INDENT_MAX,
                             "value": 20}

        line_color_attrs = {"type": "color",
                            "class": "form-control form-control-color",
                            "id": "exampleColorInput"}

        background_color_attrs = {"type": "color",
                                  "class": "form-control form-control-color",
                                  "id": "exampleColorInput"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs),
            "background_color": forms.TextInput(attrs=background_color_attrs)
        }
