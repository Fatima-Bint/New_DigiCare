from django.urls import path

from .views import home, checker


app_name = "symptoms_checker"

urlpatterns = [path("", home, name="home"), path("symptoms/checker/", checker, name="checker")]
