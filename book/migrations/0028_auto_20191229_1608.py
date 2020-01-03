# Generated by Django 2.2.9 on 2019-12-30 00:08

import book.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0027_auto_20191229_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.FileField(upload_to='chapters', validators=[book.validators.validate_file_extension]),
        ),
    ]
