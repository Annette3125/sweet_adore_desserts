from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from .models import User


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
