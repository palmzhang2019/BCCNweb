# Generated by Django 3.0.7 on 2020-06-15 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_remove_products_parmas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsdetail',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Products'),
        ),
    ]
