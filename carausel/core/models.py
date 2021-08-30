from django.db import models

# Create your models here.

class Carausel(models.Model):
    image = models.ImageField(upload_to='slider')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)
    button = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title