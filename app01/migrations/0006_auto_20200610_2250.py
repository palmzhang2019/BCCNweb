# Generated by Django 3.0.7 on 2020-06-10 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0005_auto_20200609_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='tag',
        ),
        migrations.AlterField(
            model_name='activity',
            name='main_image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='main_image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('breif', models.TextField(max_length=1024)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='类型')),
            ],
        ),
    ]