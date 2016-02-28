from django.contrib import admin
from app.mariage.models import Hotel, Carpooling, Song
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
    list_display = ('name', 'order', 'price_range','website', )
    #search_fields = ()
    readonly_fields = ('created_by', 'modified_by')
    #list_filter = ('vehicle__active_p', 'administrative_area_one')


class CarpoolingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'places', 'departure',)
    #search_fields = ()
    readonly_fields = ('created_by', 'modified_by')
    #list_filter = ('vehicle__active_p', 'administrative_area_one')


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'when', 'partition', 'four_voice', 'soprane', 'alto', 'tenor', 'basse')
    ordering = ('order',)
    #search_fields = ()
    readonly_fields = ('created_by', 'modified_by')
    #list_filter = ('vehicle__active_p', 'administrative_area_one')


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Carpooling, CarpoolingAdmin)
admin.site.register(Song, SongAdmin)

