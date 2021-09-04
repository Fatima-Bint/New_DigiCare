from django.urls import path

from .views import login_user, signup


app_name = "authentication"


urlpatterns = [path("login/", login_user, name="login"), path("signup/", signup, name="signup")]
