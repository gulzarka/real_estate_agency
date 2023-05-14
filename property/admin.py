from django.contrib import admin

from .models import Flat, Complaint, Owner


class PropertyInline(admin.TabularInline):
    model = Flat.owned_flat.through
    raw_id_fields = ['owner']


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
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [PropertyInline]
    # exclude = ['flat']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text')
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
