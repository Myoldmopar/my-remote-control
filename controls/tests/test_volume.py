from django.test import TestCase
from controls import volume


class TestVolumeController(TestCase):
    def test_instantiation(self):
        volume.VolumeController()
        self.assertTrue(True)
