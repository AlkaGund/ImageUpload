from django.contrib import admin

# Register your models here.
from .models import Hotel


class HotelAdmin(admin.ModelAdmin):
    list_display  = ['name', 'hotel_Main_Img']

admin.site.register(Hotel,HotelAdmin)
