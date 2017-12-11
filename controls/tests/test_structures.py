from django.test import TestCase

from controls import structures


class TestSuccessfulReturnTypeBase(TestCase):

    def setUp(self):
        self.s = structures.SuccessfulReturnTypeBase()

    def test_structure(self):
        if not hasattr(self.s, 'success'):
            self.fail('SuccessfulReturnTypeBase does not contain success member.')
        self.assertTrue(self.s.success)

    def test_to_dict(self):
        d = self.s.to_dict()
        self.assertIn('success', d)
        self.assertTrue(d['success'])


class TestFailureReturnTypeBaseNoMessage(TestCase):

    def setUp(self):
        self.s = structures.FailureReturnTypeBase()

    def test_structure(self):
        if not hasattr(self.s, 'success'):
            self.fail('FailureReturnTypeBase does not contain success member.')
        self.assertFalse(self.s.success)

    def test_to_dict(self):
        d = self.s.to_dict()
        self.assertIn('success', d)
        self.assertFalse(d['success'])


class TestFailureReturnTypeBaseWithMessage(TestCase):

    def setUp(self):
        self.s = structures.FailureReturnTypeBase(message='Error: Tosche Station is out of power converters.')

    def test_structure(self):
        if not hasattr(self.s, 'success'):
            self.fail('FailureReturnTypeBase does not contain success member.')
        self.assertFalse(self.s.success)
        if not hasattr(self.s, 'message'):
            self.fail('FailureReturnTypeBase does not contain message member.')

    def test_to_dict(self):
        d = self.s.to_dict()
        self.assertIn('success', d)
        self.assertFalse(d['success'])
        self.assertIn('message', d)
        self.assertIn('Tosche Station', d['message'])
