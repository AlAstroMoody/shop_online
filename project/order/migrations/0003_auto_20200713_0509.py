# Generated by Django 3.0.8 on 2020-07-13 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_productinbasket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='nmb',
            new_name='quantity_num',
        ),
    ]
