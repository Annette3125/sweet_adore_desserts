import re

from .forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.
@csrf_protect
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("register_complete"))
    else:
        form = UserCreationForm()
    context = {"form": form, "action_url": reverse("register")}
    return render(request, "registration/register.html", context={"form": form})



def register_complete(request):
    return render(request, template_name="registration/register_complete.html")