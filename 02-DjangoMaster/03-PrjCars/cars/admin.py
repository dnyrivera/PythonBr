from django.contrib import admin
from cars.models import Car, Brand

# Register your models here to show up in the /admin website to use it.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value',)
    search_fields = ('brand', 'model',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)