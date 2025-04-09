from django.contrib.auth.forms import \
    UserCreationForm as DjangoUserCreationForm
from django.forms import ModelForm

from .models import Profile, User


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = DjangoUserCreationForm.Meta.fields + ("email",)


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "bio"]
