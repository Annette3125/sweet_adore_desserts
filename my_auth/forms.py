from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

from django import forms
from .models import User

class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = DjangoUserCreationForm.Meta.fields + ("email",)

