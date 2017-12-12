import os
import unittest

from django.test import TestCase

from controls import volume


class TestVolumeController(TestCase):

    @unittest.skipIf("CI" in os.environ, "Skipping this test on Travis CI.")
    def test_instantiation(self):  # pragma: no cover
        try:
            volume.VolumeController()
        except Exception:
            self.fail('Could not instantiate VolumeController, check OS is Linux and alsa is in place.')

    @unittest.skipIf("CI" in os.environ, "Skipping this test on Travis CI.")
    def test_get_volume(self):  # pragma: no cover
        v = volume.VolumeController()
        vol = v.get_volume()
        self.assertTrue(vol.success)
        try:
            volume_value = vol.volume
            self.assertIsInstance(volume_value, int)
        except IndexError:
            self.fail('Something wrong with volume response in get_volume, some underlying Mixer problem.')

    # TODO: add more local run tests


class TestSuccessfulVolumeReturnType(TestCase):
    def setUp(self):
        self.volume = 8
        self.s = volume.SuccessfulVolumeReturnType(self.volume)

    def test_structure(self):
        if not hasattr(self.s, 'success'):
            self.fail('SuccessfulVolumeReturnType does not contain success member.')
        self.assertTrue(self.s.success)
        if not hasattr(self.s, 'volume'):
            self.fail('SuccessfulVolumeReturnType does not contain volume member.')
        self.assertEqual(self.volume, self.s.volume)

    def test_to_dict(self):
        d = self.s.to_dict()
        self.assertIn('success', d)
        self.assertTrue(d['success'])
        self.assertIn('volume', d)
        self.assertEqual(self.volume, d['volume'])


class TestSuccessfulMuteReturnType(TestCase):
    def setUp(self):
        self.mute = volume.VolumeController.Muted
        self.s = volume.SuccessfulMuteReturnType(self.mute)

    def test_structure(self):
        if not hasattr(self.s, 'success'):
            self.fail('SuccessfulMuteReturnType does not contain success member.')
        self.assertTrue(self.s.success)
        if not hasattr(self.s, 'muted'):
            self.fail('SuccessfulMuteReturnType does not contain muted member.')
        self.assertEqual(self.mute, self.s.muted)

    def test_to_dict(self):
        d = self.s.to_dict()
        self.assertIn('success', d)
        self.assertTrue(d['success'])
        self.assertIn('muted', d)
        self.assertEqual(self.mute, d['muted'])
