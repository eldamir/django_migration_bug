from django.test import TestCase
from reproduction.models import TestModel


class TestModelUnitTest(TestCase):
    def test_models_are_there(self):
        self.assertEqual(TestModel.objects.count(), 4)

    def test_models_are_still_there(self):
        self.assertEqual(TestModel.objects.count(), 4)