from django import forms
from .models import LineEffectModel, BackgroundFillingEffectModel, NeonLineEffectModel, PaletteRainbowEffectModel

LINE_WIDTH_MIN = 1
LINE_WIDTH_MAX = 300

LINE_INDENT_MIN = 10
LINE_INDENT_MAX = 100

NEON_RATE_MIN = 10
NEON_RATE_MAX = 300

PALETTE_SIZE_MIN = 1
PALETTE_SIZE_MAX = 10


class LineEffectForm(forms.ModelForm):
    class Meta:
        model = LineEffectModel
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
                            "id": "lineColor"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs)
        }


class BackgroundFillingEffectForm(forms.ModelForm):
    class Meta:
        model = BackgroundFillingEffectModel
        fields = ("image", "line_width", "line_indent", "line_color", "background_color", "apply_bw_filter")

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
                            "id": "lineColor"}

        background_color_attrs = {"type": "color",
                                  "class": "form-control form-control-color",
                                  "id": "backgroundColor"}

        apply_bw_filter_attrs = {"type": "checkbox"}
                                 # "name": "applyBwFilter[]",
                                 # "value": "true"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs),
            "background_color": forms.TextInput(attrs=background_color_attrs),
            "apply_bw_filter": forms.CheckboxInput(attrs=apply_bw_filter_attrs)
        }


class NeonLineEffectForm(forms.ModelForm):
    class Meta:
        model = NeonLineEffectModel
        fields = ("image", "line_width", "line_indent", "neon_rate", "line_color")

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

        neon_rate_attrs = {"type": "range",
                           "class": "form-control-range",
                           "id": "neonRate",
                           "min": NEON_RATE_MIN,
                           "max": NEON_RATE_MAX,
                           "value": 100}

        line_color_attrs = {"type": "color",
                            "class": "form-control form-control-color",
                            "id": "lineColor"}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "neon_rate": forms.NumberInput(attrs=neon_rate_attrs),
            "line_color": forms.TextInput(attrs=line_color_attrs)
        }


class PaletteRainbowEffectForm(forms.ModelForm):
    class Meta:
        model = PaletteRainbowEffectModel
        fields = ("image", "line_width", "line_indent", "palette_size")

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

        palette_size_attrs = {"type": "range",
                              "class": "form-control-range",
                              "id": "paletteSize",
                              "min": PALETTE_SIZE_MIN,
                              "max": PALETTE_SIZE_MAX,
                              "value": 5}

        widgets = {
            "image": forms.FileInput(attrs=image_attrs),
            "line_width": forms.NumberInput(attrs=line_width_attrs),
            "line_indent": forms.NumberInput(attrs=line_indent_attrs),
            "palette_size": forms.NumberInput(attrs=palette_size_attrs)
        }
