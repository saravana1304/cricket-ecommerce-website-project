# Generated by Django 5.0.2 on 2024-04-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]