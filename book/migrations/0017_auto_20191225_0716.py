# Generated by Django 3.0.1 on 2019-12-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0016_collection_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]