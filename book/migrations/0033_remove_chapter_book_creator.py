# Generated by Django 2.2.9 on 2020-01-02 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0032_chapter_book_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='book_creator',
        ),
    ]
