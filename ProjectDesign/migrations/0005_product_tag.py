# Generated by Django 3.2.6 on 2021-10-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectDesign', '0004_auto_20211004_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('featured', 'featured'), ('recent', 'recent')], default='featured', max_length=20),
        ),
    ]
