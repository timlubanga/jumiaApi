# Generated by Django 3.1.4 on 2021-02-16 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20210211_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
