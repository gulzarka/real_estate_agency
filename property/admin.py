from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone')
    list_editable = (
        'price',
        'new_building',
        'construction_year',
        'town')
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony')
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text')

    raw_id_fields = ('user', 'flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
