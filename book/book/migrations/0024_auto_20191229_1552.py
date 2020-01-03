# Generated by Django 2.2.9 on 2019-12-29 23:52

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_auto_20191226_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('content', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/chapters'), upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='chapter',
            field=models.ManyToManyField(related_name='book_chapter', to='book.Chapter'),
        ),
    ]