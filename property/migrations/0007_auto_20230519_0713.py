# Generated by Django 2.2.24 on 2023-05-19 04:13

from django.db import migrations
import phonenumbers


def fill_normalized_phone(apps, schema_editor):
    flat = apps.get_model('property', 'Flat')
    for flat in flat.objects.all().iterator():
        parsed_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_phonenumber):
            flat.owner_pure_phone = parsed_phonenumber
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owner_pure_phone'),
    ]

    operations = [migrations.RunPython(fill_normalized_phone)
    ]
