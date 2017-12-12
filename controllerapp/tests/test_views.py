import json
import os
from alsaaudio import ALSAAudioError

from django.core.urlresolvers import reverse
from django.test import TestCase


class SwaggerViewTests(TestCase):
    def test_swagger(self):
        endpoint_name = 'swagger'
        if os.environ.get('CI') is 'true':
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
        if os.environ.get('CI') is 'true':
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_down(self):
        endpoint_name = 'volume-down'
        if os.environ.get('CI') is 'true':
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_mute(self):
        endpoint_name = 'volume-toggle-mute'
        if os.environ.get('CI') is 'true':
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)
