# Generated by Django 4.0.3 on 2022-08-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrgen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='qr',
            field=models.ImageField(blank=True, upload_to='qr_code'),
        ),
    ]
