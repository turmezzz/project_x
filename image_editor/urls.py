from django.urls import path

from . import views


urlpatterns = [
    path("", views.line_effect, name="home"),
    path("line_effect", views.line_effect, name="line_effect"),
    path("background_filling_effect", views.background_filling_effect, name="background_filling_effect"),
    path("neon_line_effect", views.neon_line_effect, name="neon_line_effect"),
    path("palette_rainbow_effect", views.palette_rainbow_effect, name="palette_rainbow_effect")

]
