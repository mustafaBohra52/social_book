# Generated by Django 5.0 on 2023-12-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_registerform_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerform',
            name='visibility',
            field=models.BooleanField(default='False'),
        ),
    ]
