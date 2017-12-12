import json
import os
from alsaaudio import ALSAAudioError

from django.core.urlresolvers import reverse
from django.test import TestCase


class ControlsViewTests(TestCase):
    def test_control_page(self):
        endpoint_name = 'controls'
        response = self.client.get(reverse(endpoint_name))
        self.assertEqual(response.status_code, 200)


class SwaggerViewTests(TestCase):
    def test_swagger(self):
        endpoint_name = 'swagger'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)
            try:
                json_content = json.loads(response.content)
                self.assertEqual("document", json_content["_type"])
            except Exception:
                self.fail('Malformed Swagger response')


class TestVolumeViewSet(TestCase):
    def test_up(self):
        endpoint_name = 'volume-up'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_down(self):
        endpoint_name = 'volume-down'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_mute(self):
        endpoint_name = 'volume-toggle-mute'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)


class TestMediaViewSet(TestCase):
    def test_next_song(self):
        endpoint_name = 'media-next-song'
        response = self.client.get(reverse(endpoint_name))
        if 'CI' in os.environ:
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)

    def test_play_pause(self):
        endpoint_name = 'media-play-pause'
        response = self.client.get(reverse(endpoint_name))
        if 'CI' in os.environ:
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)
