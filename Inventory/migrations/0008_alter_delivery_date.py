# Generated by Django 5.0.1 on 2024-01-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_alter_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='date',
            field=models.DateField(),
        ),
    ]
