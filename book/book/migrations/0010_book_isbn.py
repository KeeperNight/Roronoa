# Generated by Django 3.0.1 on 2019-12-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20191222_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=234123123123),
            preserve_default=False,
        ),
    ]
