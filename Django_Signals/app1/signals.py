import time
from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def user_post_save(sender, instance, created, **kwargs):
#     print("Signal handler started.")
#     time.sleep(5)  # making it sleep for 5 seconds
#     print("Signal handler completed.")