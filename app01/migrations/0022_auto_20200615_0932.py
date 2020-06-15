# Generated by Django 3.0.7 on 2020-06-15 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_auto_20200614_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sale_num',
            field=models.PositiveIntegerField(default=0, verbose_name='销售额'),
        ),
        migrations.AddField(
            model_name='products',
            name='store_num',
            field=models.PositiveIntegerField(default=0, verbose_name='库存量'),
        ),
    ]
