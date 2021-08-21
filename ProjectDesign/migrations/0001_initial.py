# Generated by Django 3.2.6 on 2021-08-20 05:04

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='The Young Baker', max_length=20, unique=True)),
                ('subtitle', models.CharField(default='For Delicious Cakes', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='Home/')),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
