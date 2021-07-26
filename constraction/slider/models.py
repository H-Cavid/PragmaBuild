from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class Slider(models.Model):
    url=URLField(max_length=200)
    image=models.ImageField(upload_to='slider')

    def __str__(self):
        return self.url