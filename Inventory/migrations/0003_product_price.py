# Generated by Django 5.0.1 on 2024-01-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_rename_sites_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
