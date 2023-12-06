from django.contrib import admin

from cars.models import Car


@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
