# Generated by Django 4.1 on 2022-08-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrgen', '0009_qrcode_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QrCode',
        ),
    ]
