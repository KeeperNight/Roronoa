# Generated by Django 2.2.9 on 2020-01-01 23:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('book', '0030_auto_20191231_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]