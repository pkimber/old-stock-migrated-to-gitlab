# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ProductBundle'
        db.delete_table('stock_productbundle')

        # Removing M2M table for field bundle on 'ProductBundle'
        db.delete_table(db.shorten_name('stock_productbundle_bundle'))


    def backwards(self, orm):
        # Adding model 'ProductBundle'
        db.create_table('stock_productbundle', (
            ('legacy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.Product'], related_name='+')),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
        ))
        db.send_create_signal('stock', ['ProductBundle'])

        # Adding M2M table for field bundle on 'ProductBundle'
        m2m_table_name = db.shorten_name('stock_productbundle_bundle')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productbundle', models.ForeignKey(orm['stock.productbundle'], null=False)),
            ('product', models.ForeignKey(orm['stock.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productbundle_id', 'product_id'])


    models = {
        'stock.product': {
            'Meta': {'object_name': 'Product', 'ordering': "('legacy', 'category__slug', 'name')"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.ProductCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'stock.productcategory': {
            'Meta': {'object_name': 'ProductCategory', 'ordering': "('name',)"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.ProductType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        },
        'stock.producttype': {
            'Meta': {'object_name': 'ProductType', 'ordering': "('name',)"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        }
    }

    complete_apps = ['stock']