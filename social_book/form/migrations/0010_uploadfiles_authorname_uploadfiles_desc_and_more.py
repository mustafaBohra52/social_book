# Generated by Django 5.0 on 2023-12-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_alter_registerform_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfiles',
            name='authorName',
            field=models.CharField(default='**', max_length=20),
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='title',
            field=models.CharField(default='title', max_length=50),
        ),
    ]
