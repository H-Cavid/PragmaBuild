from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50,blank=True,null=True)
    product_price = models.CharField(max_length=50,blank=True,null=True)
    product_image=models.ImageField(upload_to='product',blank=True,null=True)

    def __str__(self) -> str:
        return self.product_name