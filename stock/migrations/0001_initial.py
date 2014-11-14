# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('legacy', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product',
                'ordering': ('legacy', 'category__slug', 'name'),
                'verbose_name_plural': 'Product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Product category',
                'ordering': ('name',),
                'verbose_name_plural': 'Product categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Product type',
                'ordering': ('name',),
                'verbose_name_plural': 'Product types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='product_type',
            field=models.ForeignKey(to='stock.ProductType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='stock.ProductCategory'),
            preserve_default=True,
        ),
    ]
