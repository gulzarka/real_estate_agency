# Generated by Django 2.2.24 on 2023-05-19 19:46

from django.db import migrations


def migrate_data_from_flat_to_owner(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    owners = apps.get_model('property', 'Owner')
    for flat in flats.objects.all().iterator():
        owners.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone)


def move_backward(apps, schema_editor):
    owners = apps.get_model('property', 'Owner')
    owners.objects.all().delete()
    owners.objects.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_owner'),
    ]

    operations = [migrations.RunPython(
        migrate_data_from_flat_to_owner,
        move_backward)]
