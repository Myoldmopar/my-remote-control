import os
from unittest import skipIf

from django.test import TestCase

from controls import volume


class TestVolumeController(TestCase):
    def test_a(self):
        pass

    @skipIf(os.environ.get('TRAVIS') is 'true', 'Cannot run this test on Travis.')
    def test_instantiation(self):  # pragma: no cover
        try:
            volume.VolumeController()
        except Exception:
            self.fail('Could not instantiate VolumeController, check OS is Linux and alsa is in place.')

    @skipIf(os.environ.get('TRAVIS') is 'true', 'Cannot run this test on Travis.')
    def test_get_volume(self):  # pragma: no cover
        v = volume.VolumeController()
        vol = v.get_volume()
        self.assertTrue(vol.success)
        try:
            volume_value = vol.volume
            self.assertIsInstance(volume_value, int)
        except IndexError:
            self.fail('Something wrong with volume response in get_volume, some underlying Mixer problem.')
