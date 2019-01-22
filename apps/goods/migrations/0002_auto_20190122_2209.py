# Generated by Django 2.0.5 on 2019-01-22 22:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
        migrations.AlterModelOptions(
            name='goodscategorybrand',
            options={'verbose_name': '品牌', 'verbose_name_plural': '品牌'},
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner', verbose_name='轮播图片'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='code',
            field=models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='is_tab',
            field=models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='name',
            field=models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='desc',
            field=models.TextField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='name',
            field=models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名'),
        ),
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table='goods_goodsbrand',
        ),
        migrations.AddField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods'),
        ),
    ]
