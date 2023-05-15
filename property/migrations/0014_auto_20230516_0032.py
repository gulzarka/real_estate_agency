# Generated by Django 3.2.10 on 2023-05-15 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0013_auto_20230513_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complainted', to='property.flat', verbose_name='квартира на которую жаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainted', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='has_balcony',
            field=models.BooleanField(db_index=True, null=True, verbose_name='Наличие балкона'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes_flat', to=settings.AUTH_USER_MODEL, verbose_name='кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owned_flat',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
