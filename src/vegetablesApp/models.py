from django.db import models
from datetime import date

# Create your models here.
class Vegetables(models.Model):
    VEG_TYPE_CHOICES = [
        ('Peas','Peas'),
        ('Broad Beans', 'Broad Beans'),
        ('Runner Beans', 'Runner Beans'),
        ('Radish','Radish'),
        ('Lettuce', 'Lettuce'),
        ('Cabbage', 'Cabbage'),
        ('Tomato', 'Tomato'),
        ('Vegetable','Vegetable')
    ]
    SEED_OR_SEEDLING_CHOICES = [
        ('Seed','Grown from seed'),
        ('Seedling', 'Grown from seedling')
    ]
    type = models.CharField('Type of Vegetable',max_length=30,choices=VEG_TYPE_CHOICES,default='Vegetable')
    variety = models.CharField('Variety of vegetable',null=True, blank=True, max_length=50)
    seed_seedling = models.CharField('Seed or Seedling',choices=SEED_OR_SEEDLING_CHOICES, max_length=8, default='seed')
    sowing_date = models.DateField('Sowing Date',default=date.today())
    harvest_date = models.DateField('Harvesting Date', default=date.today())
    pests = models.CharField('Pests',max_length=50,default='No pests')
    tips = models.TextField('Tips', default='No tips')
    comments = models.TextField('Comments', default='No comments')

    def __str__(self):
        return self.type



