# Generated by Django 3.0.1 on 2019-12-25 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20191225_0724'),
        ('user', '0006_auto_20191225_0724'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
