# Generated by Django 2.2.24 on 2023-05-11 18:43

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20230511_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
