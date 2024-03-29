# Generated by Django 4.2.6 on 2024-03-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_listed', models.BooleanField(default=True, verbose_name='Is Listed')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
