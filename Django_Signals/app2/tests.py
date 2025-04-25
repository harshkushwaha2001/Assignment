from django.test import TestCase
from .models import User
import threading

# class ThreadCheckTest(TestCase):
#     def test_signal_runs_in_same_thread(self):
#         print(f"[Caller] Caller Thread ID: {threading.get_ident()}")
#         User.objects.create(username='Harsh Kushwaha',email='harshkushwaha32001@gmail.com',address='earth')
