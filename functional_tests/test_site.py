from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from reproduction.models import TestModel


class TestModelTest(StaticLiveServerTestCase):
    def test_models_are_there(self):
        self.assertEqual(TestModel.objects.count(), 4)

    def test_models_are_still_there(self):
        self.assertEqual(TestModel.objects.count(), 4)
