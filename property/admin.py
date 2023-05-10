from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town')
    list_editable = (
        'price',
        'new_building',
        'construction_year',
        'town')

     


admin.site.register(Flat, FlatAdmin)
