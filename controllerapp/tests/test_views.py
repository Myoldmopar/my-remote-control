import json
import os
from alsaaudio import ALSAAudioError

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class ControlsViewTests(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_control_page(self):
        endpoint_name = 'controls:controls'
        response = self.client.get(reverse(endpoint_name))
        self.assertEqual(response.status_code, 200)


class SwaggerViewTests(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_swagger(self):
        endpoint_name = 'controls:swagger'
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
    def setUp(self):
        self.u = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_up(self):
        endpoint_name = 'controls:api:volume-up'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_down(self):
        endpoint_name = 'controls:api:volume-down'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)

    def test_mute(self):
        endpoint_name = 'controls:api:volume-toggle-mute'
        if 'CI' in os.environ:
            with self.assertRaises(ALSAAudioError):
                self.client.get(reverse(endpoint_name))
        else:
            response = self.client.get(reverse(endpoint_name))
            self.assertEqual(response.status_code, 200)


class TestMediaViewSet(TestCase):
    def setUp(self):
        self.u = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    def test_next_song(self):
        endpoint_name = 'controls:api:media-next-song'
        response = self.client.get(reverse(endpoint_name))
        if 'CI' in os.environ or 'TOX' in os.environ:
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)

    def test_play_pause(self):
        endpoint_name = 'controls:api:media-play-pause'
        response = self.client.get(reverse(endpoint_name))
        if 'CI' in os.environ or 'TOX' in os.environ:
            self.assertEqual(response.status_code, 500)
        else:
            self.assertEqual(response.status_code, 200)
