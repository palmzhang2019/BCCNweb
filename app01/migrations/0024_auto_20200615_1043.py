# Generated by Django 3.0.7 on 2020-06-15 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0023_auto_20200615_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='parmas',
        ),
        migrations.RemoveField(
            model_name='productsparams',
            name='name',
        ),
        migrations.AddField(
            model_name='productsparams',
            name='meta_key',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='参数名'),
        ),
        migrations.AddField(
            model_name='productsparams',
            name='meta_value',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='参数值'),
        ),
        migrations.AlterField(
            model_name='params2products',
            name='param',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.ProductsParams'),
        ),
        migrations.AlterField(
            model_name='params2products',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Products'),
        ),
        migrations.RemoveField(
            model_name='productsparams',
            name='product',
        ),
        migrations.AddField(
            model_name='productsparams',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Products'),
        ),
        migrations.DeleteModel(
            name='ProductParmas',
        ),
    ]