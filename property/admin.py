from django.contrib import admin

from .models import Flat, Complaint
# Owner


# class PropertyInline(admin.TabularInline):
#     model = Flat.owners.through
#     raw_id_fields = ['owner']


@admin.register(Flat)
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
        'town',
        'owners_phonenumber',
        'owner_pure_phone')
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony')
    raw_id_fields = ('liked_by',)
    # inlines = [PropertyInline]
    # exclude = ['flat']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text')
    raw_id_fields = ('user', 'flat')


# @admin.register(Owner)
# class OwnerAdmin(admin.ModelAdmin):
#     raw_id_fields = ('flat',)

