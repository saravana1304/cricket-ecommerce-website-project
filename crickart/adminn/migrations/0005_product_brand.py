# Generated by Django 5.0.2 on 2024-03-21 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminn', '0004_brand_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminn.brand'),
            preserve_default=False,
        ),
    ]
