from vegetablesApp.views import vegetables_home_view
from mixer.backend.django import mixer
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, SimpleTestCase


class TestViews(TestCase):
    def test_home_view_unautheticated(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser
        response = vegetables_home_view(request)
        self.assertEqual(response.status_code,200,'Home - unautheticated')

    def test_add_view_unautheticated(self):
        request = RequestFactory().get('add')
        request.user = AnonymousUser
        response = vegetables_home_view(request)
        self.assertEqual(response.status_code, 200, 'Add - unautheticated')

    def test_list_view_unautheticated(self):
        request = RequestFactory().get('list')
        request.user = AnonymousUser
        response = vegetables_home_view(request)
        self.assertEqual(response.status_code, 200, 'List - unautheticated')



class TestTemplates(SimpleTestCase):
    def test_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'vegetablesApp/home.html')

    def test_add_template(self):
        response = self.client.get('/add/')
        self.assertTemplateUsed(response, 'vegetablesApp/add_veg.html')

    def test_list_template(self):
        response = self.client.get('/list/')
        self.assertTemplateUsed(response, 'vegetablesApp/list_veg.html')