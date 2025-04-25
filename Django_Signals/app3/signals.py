from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def create_another_user(sender, instance, created, **kwargs):
    if instance.username != "AutoUser":
        print("Signal triggered! Creating AutoUser...")
        User.objects.create(
            username="AutoUser",
            email="auto@example.com",
            address="Auto-created from signal"
        )