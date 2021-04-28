from vegetablesApp.models import Vegetables
import factory
from faker import Faker
from faker.providers import BaseProvider
import random


fake = Faker()

class VegetableProvider(BaseProvider):
    def vegetable(self):
        vegetables = [
            'pea','runner bean', 'broad bean','lettuce', 'radish'
        ]
        return random.choice(vegetables)



class VegetablesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vegetables

    fake.add_provider(VegetableProvider)
    name = fake.vegetable()

