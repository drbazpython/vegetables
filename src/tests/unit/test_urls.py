from django.test import SimpleTestCase
import pytest
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_home_view_url_resolves(self):
        self.assertEqual(resolve('/').func.__name__ , 'vegetables_home_view')


    def test_add_view_url_resolves(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.__name__, 'vegetables_add_view')

    def test_list_view_url_resolves(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func.__name__, 'vegetables_list_view')