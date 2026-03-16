from django.contrib import admin
from .models import Plant, Review, PlantCare

admin.site.register(Plant)
admin.site.register(Review)
admin.site.register(PlantCare)