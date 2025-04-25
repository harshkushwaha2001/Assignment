from django.test import TestCase
from django.db import transaction
from app1.models import User

class SignalTransactionTest(TestCase):
    def test_signal_and_main_user_rollback(self):
        try:
            with transaction.atomic():
                User.objects.create(
                    username='Harsh Kushwaha',
                    email='harshkushwaha32001@gmail.com',
                    address='earth'
                )
                raise Exception("Force rollback")
        except:
            pass

        # Check if main user or auto-created user exist
        user_exists = User.objects.filter(username='Harsh Kushwaha').exists()
        auto_user_exists = User.objects.filter(username='AutoUser').exists()

        print(f"Main user exists? {user_exists}")
        print(f"AutoUser exists? {auto_user_exists}")

        self.assertFalse(user_exists, "Main user was not rolled back!")
        self.assertFalse(auto_user_exists, "AutoUser from signal should also be rolled back!")
