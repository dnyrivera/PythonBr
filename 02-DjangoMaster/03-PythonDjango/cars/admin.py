from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ("desc_brand",)
    search_fields = ("desc_brand",)


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", "price")
    search_fields = (
        "model",
        "brand",
    )


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
