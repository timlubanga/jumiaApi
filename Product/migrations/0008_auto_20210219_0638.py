# Generated by Django 3.1.4 on 2021-02-19 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_auto_20210219_0626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='productreviews',
            new_name='product',
        ),
    ]