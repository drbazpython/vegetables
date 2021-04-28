from django.forms import ModelForm
from vegetablesApp.models import Vegetables

class VegetablesAddForm(ModelForm):
    class Meta:
        model = Vegetables
        fields = ['type',
                  'variety',
                  'seed_seedling',
                  'sowing_date',
                  'harvest_date',
                  'pests',
                  'tips',
                  'comments'
                  ]


