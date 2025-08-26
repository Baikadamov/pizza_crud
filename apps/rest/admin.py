from django.contrib import admin

from apps.rest.models import *

# Register your models here.


admin.site.register(Pizza)
admin.site.register(Restaurant)
admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Review)