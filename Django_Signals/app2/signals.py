import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def book_post_save(sender, instance, **kwargs):
    print(f"[SIGNAL] Signal Thread ID: {threading.get_ident()}")