# Generated by Django 4.1 on 2022-08-11 19:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrgen', '0014_qrcode_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QrCode',
            new_name='Create_link',
        ),
    ]
