# Generated by Django 5.0 on 2023-12-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_registerform_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='visibility',
            field=models.BooleanField(),
        ),
    ]
