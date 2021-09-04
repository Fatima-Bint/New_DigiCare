from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    template = "index.html"
    context = {}
    return render(request=request, template_name=template, context=context)


@login_required
def checker(request):
    template = "checker.html"
    context = {}
    return render(request=request, template_name=template, context=context)
