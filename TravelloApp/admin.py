from django.contrib import admin
from .models import Destination


# Register your models here.
class list(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Destination,list)
