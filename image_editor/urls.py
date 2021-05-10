from django.urls import path

from . import views


urlpatterns = [
    path("", views.line_effect, name="home"),
    path("line_effect", views.line_effect, name="line_effect"),
    path("background_filling_effect", views.background_filling_effect, name="background_filling_effect")
]
