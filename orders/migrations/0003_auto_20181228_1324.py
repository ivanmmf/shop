# Generated by Django 2.1.3 on 2018-12-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181228_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
    ]
