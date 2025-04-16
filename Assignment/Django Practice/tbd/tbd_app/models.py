from django.db import models

# Create your models here.
class Car(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
