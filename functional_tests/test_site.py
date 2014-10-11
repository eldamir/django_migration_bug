import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from reproduction.models import TestModel


class FunctionalTest(StaticLiveServerTestCase):
    pass


class TestModelTest(FunctionalTest):
    def test_models_are_there(self):
        self.assertEqual(TestModel.objects.count(), 4)

    def test_models_are_still_there(self):
        self.assertEqual(TestModel.objects.count(), 4)