# Generated by Django 5.0 on 2023-12-13 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]