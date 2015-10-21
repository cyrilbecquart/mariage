from django.contrib import admin
from app.mariage.models import Hotel
from django import forms


class HotelAdminForm( forms.ModelForm ):
    class Meta:
        model = Hotel
        fields = "__all__" 
        widgets = {
            'description': forms.Textarea(),
            'address': forms.Textarea(),
        }

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    form = HotelAdminForm
    list_display = ('name', 'email', 'phone', 'website', 'address', 'price_range',)
    #search_fields = ()
    readonly_fields = ('created_by', 'modified_by')
    #list_filter = ('vehicle__active_p', 'administrative_area_one')

admin.site.register(Hotel, HotelAdmin)
