from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
  def test_addition(self):
    self.assertEqual(1+2, 3)