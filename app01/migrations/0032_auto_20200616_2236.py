# Generated by Django 3.0.7 on 2020-06-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0031_auto_20200616_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='breif',
            field=models.TextField(max_length=1024, null=True),
        ),
    ]
