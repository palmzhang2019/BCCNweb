# Generated by Django 3.0.7 on 2020-06-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20200611_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='main_image',
            field=models.ImageField(null=True, upload_to='activity'),
        ),
    ]
