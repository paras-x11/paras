from django.db import models

# Create your models here.
class Car(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    # car_image = models.ImageField(upload_to="car_images", blank=True) #, height_field=None, width_field=None, max_length=None)
    model_year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    mileage = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"





