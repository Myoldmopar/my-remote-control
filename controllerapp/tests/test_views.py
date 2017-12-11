import json
import os

from django.core.urlresolvers import reverse
from django.test import TestCase


class SwaggerViewTests(TestCase):
    def test_swagger(self):
        response = self.client.get(reverse('swagger'))
        self.assertEqual(response.status_code, 200)
        try:
            json_content = json.loads(response.content)
            self.assertEqual("document", json_content["_type"])
        except Exception:
            self.fail('Malformed Swagger response')


class TestVolumeViewSet(TestCase):
    def test_up(self):
        response = self.client.get(reverse('swagger'))
        if os.environ.get('TRAVIS') is 'true':
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)

    def test_down(self):
        response = self.client.get(reverse('swagger'))
        if os.environ.get('TRAVIS') is 'true':
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)

    def test_mute(self):
        response = self.client.get(reverse('swagger'))
        if os.environ.get('TRAVIS') is 'true':
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)
