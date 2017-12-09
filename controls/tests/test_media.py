from django.test import TestCase
from controls import media


class MyTest(TestCase):
    def test_a(self):
        media.MediaController()
        self.assertTrue(True)
