from audioop import minmax
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, default='');
    short_discription = models.CharField(max_length=250, default='');
    long_discription = models.CharField(max_length=1000, default='');
    image = models.ImageField(default='');
    date_added = models.DateTimeField(auto_now=True);
    held_in_stock = models.IntegerField(default=0);
    sold = models.IntegerField(default=0);
    raw_price_per_unit = models.FloatField(default=1.0);
    profit_per_unit = models.FloatField(default=1.0);
    tax_percentage = models.FloatField(default=20.0);

    @property
    def imageUrl(self):
        try:
            url = self.image.url;
        except:
            url = '';
        return url;