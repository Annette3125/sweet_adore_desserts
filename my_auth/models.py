from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="desserts/profile.pics", blank=True, null=True)
    bio = models.TextField("about", max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.photo.path)
            size = 300
            if img.height > size or img.width > size:
                output_size = (size, size)
                img.thumbnail(output_size)
                img.save(self.photo.path)
        except ValueError:
            pass