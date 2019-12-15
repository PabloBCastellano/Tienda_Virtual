from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    image = models.CharField(max_length=300)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    characteristic=models.TextField(max_length=1000)