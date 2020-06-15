# Generated by Django 3.0.7 on 2020-06-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20200614_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='weights',
            field=models.SmallIntegerField(choices=[(0, '普通会员'), (1, '青铜会员'), (2, '白银会员'), (3, '金牌会员')], default=0),
        ),
    ]
