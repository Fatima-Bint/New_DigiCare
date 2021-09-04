from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import SignupForm, LoginForm

# Create your views here.
def login_user(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get("email"), password=form.cleaned_data.get("password"))
            # import pdb; pdb.set_trace()
            if user is not None:
                login(request=request, user=user)
                return redirect(reverse("symptoms_checker:checker"))

    template = "login.html"
    signup_form = SignupForm()
    login_form = LoginForm()

    context = {"signup_form": signup_form, "login_form": login_form}
    return render(request=request, template_name=template, context=context)


def signup(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST["username"] = request.POST["email"]
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("authentication:login"))
