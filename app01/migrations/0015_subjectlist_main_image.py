# Generated by Django 3.0.7 on 2020-06-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20200612_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectlist',
            name='main_image',
            field=models.ImageField(null=True, upload_to='subject'),
        ),
    ]
