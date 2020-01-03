# Generated by Django 3.0.1 on 2019-12-21 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default='not set', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(default='default.jpg', upload_to='Book_covers')),
                ('published', models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], max_length=2)),
                ('date_added', models.DateField()),
                ('pages', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='author.Author')),
                ('book_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('favorite', models.ManyToManyField(related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ManyToManyField(related_name='book_genre', to='book.Genre')),
                ('status', models.ManyToManyField(blank=True, choices=[('C', 'Completed'), ('R', 'Reading...'), ('CC', 'Yet to complete'), ('NS', 'Not Started')], max_length=4, related_name='status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
