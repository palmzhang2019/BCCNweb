# Generated by Django 3.0.7 on 2020-06-15 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0027_auto_20200615_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='author',
            field=models.ForeignKey(blank=True, max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Account', verbose_name='作者'),
        ),
    ]
