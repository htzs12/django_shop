# Generated by Django 2.2 on 2019-05-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190122_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/', verbose_name='轮播图片'),
        ),
    ]