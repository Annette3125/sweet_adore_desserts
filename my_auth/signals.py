from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Call this function (`create_profile`), if the `sender` is User.
    Automatically creates a profile for a new user.
    `post_save` signal is sent at the end of the Model.save() method.
        When a new object is created, or an existing object is updated, Django
        will emit the `post_save` signal.
    `instance` is the User object that was just created.
    `created` is a boolean, which is True if a new record was created.
    """
    if created:
        Profile.objects.create(user=instance)
        print(f"Profile created for {instance.username}")
    else:
        instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """Call this function (`save_profile`), if the `sender` is User.
    Automatically updates a profile after the user is updated.
    `post_save` signal is sent at the end of the Model.save() method.
        When a new object is created, or an existing object is updated, Django
        will emit the `post_save` signal.
    `instance` is the User object that was just updated (modified).
    """
    instance.profile.save()
