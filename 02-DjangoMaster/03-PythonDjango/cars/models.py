from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    desc_brand = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.desc_brand}"


# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    factory_year = models.PositiveIntegerField(blank=True, null=True)
    model_year = models.PositiveIntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="cars/", blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.model}"
