from vegetablesApp.models import Vegetables
from django.test import TestCase
import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestModel(TestCase):

    def setUp(self):
        self.veg1 = Vegetables.objects.create(
            name = 'Cabbage',
        )

    def test_init(self):
        obj = mixer.blend('vegetablesApp.Vegetables')
        assert obj.pk == 2

    def test_name(self):
        assert str(self.veg1) == self.veg1.name