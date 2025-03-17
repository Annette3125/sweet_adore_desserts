from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm



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

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                message="Profile of {username_bold} updated".format(
                    username_bold=f"<strong>{request.user}</strong>"), )
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "desserts/profile.html", context=context)
