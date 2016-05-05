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
    list_display = ('name', 'order', 'active', 'when', 'partition_p', 'four_voice_p', 'soprane_p', 'alto_p', 'tenor_p', 'basse_p')
    ordering = ('order',)
    #search_fields = ()
    readonly_fields = ('created_by', 'modified_by')
    
    def partition_p(self, obj):
        if obj.partition:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.partition.url
        return ''
    partition_p.short_description = 'Partition'
    partition_p.allow_tags = True

    def four_voice_p(self, obj):
        if obj.four_voice:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.four_voice.url
        return ''
    four_voice_p.short_description = '4 voix'
    four_voice_p.allow_tags = True

    def soprane_p(self, obj):
        if obj.soprane:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.soprane.url
        return ''
    soprane_p.short_description = 'Soprane'
    soprane_p.allow_tags = True

    def alto_p(self, obj):
        if obj.alto:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.alto.url
        return ''
    alto_p.short_description = 'Alto'
    alto_p.allow_tags = True

    def tenor_p(self, obj):
        if obj.tenor:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.tenor.url
        return ''
    tenor_p.short_description = 'Tenor'
    tenor_p.allow_tags = True

    def basse_p(self, obj):
        if obj.basse:
            return u'<a href="%s" target="_blank">Voir</a>' % obj.basse.url
        return ''
    basse_p.short_description = 'Basse'
    basse_p.allow_tags = True

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Carpooling, CarpoolingAdmin)
admin.site.register(Song, SongAdmin)

