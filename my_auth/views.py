from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_protect

from .forms import UserCreationForm



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


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/login.html'