# Generated by Django 3.0.1 on 2019-12-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_auto_20191223_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='read',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='collection',
            name='book_name',
            field=models.ManyToManyField(to='book.Book'),
        ),
    ]