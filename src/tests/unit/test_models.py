from vegetablesApp.models import Vegetables
from django.test import TestCase
import pytest
from mixer.backend.django import mixer
import factories


@pytest.mark.django_db
class TestModel(TestCase):

    def setUp(self):
        self.veg1 = Vegetables.objects.create(
            type = 'Cabbage',
        )

    def test_init(self):
        obj = mixer.blend('vegetablesApp.Vegetables')
        assert obj.pk == 2

    def test_type(self):
        assert str(self.veg1) == self.veg1.type

def test_new_vegetable(vegetables_factory):
    print(vegetables_factory.name)
    assert True