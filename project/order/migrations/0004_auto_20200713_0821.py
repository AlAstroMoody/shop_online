# Generated by Django 3.0.8 on 2020-07-13 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200713_0509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='quantity_num',
            new_name='quantity',
        ),
    ]
