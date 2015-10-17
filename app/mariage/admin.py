from django.contrib import admin
from app.mariage.models import Hotel


# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website', 'address', 'price_range',)
    #search_fields = ()
    #readonly_fields = ()
    #list_filter = ('vehicle__active_p', 'administrative_area_one')

admin.site.register(Hotel, HotelAdmin)
