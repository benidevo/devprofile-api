from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
  def test_addition(self):
    one = 1
    two = 2
    self.assertEqual(one + two, 3)
