from django.contrib import admin
from .models import Duck, Public_Relations, Hat

# Register your models here.
admin.site.register(Duck)
admin.site.register(Public_Relations)
admin.site.register(Hat)