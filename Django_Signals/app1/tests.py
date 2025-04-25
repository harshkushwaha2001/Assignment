from django.test import TestCase
import time
from .models import User
# Create your tests here.
# class SignalTimingTest(TestCase):
#      def test_signal_timing(self):
#          start = time.time()
#          User.objects.create(username='Harsh Kushwaha1',email='harshkushwaha32001@gmail.com',address='earth')
#          User.objects.create(username='Harsh Kushwaha2',email='harshkushwaha32001@gmail.com',address='earth')
#          end = time.time()
#          print(f"Total time taken: {end - start:.2f} seconds")

#          self.assertTrue((end - start) >= 10, "Signal did not delay for 5 seconds")