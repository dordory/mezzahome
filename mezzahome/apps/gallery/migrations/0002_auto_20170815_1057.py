# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20141227_0224'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendGalleryImage',
            fields=[
                ('galleryimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='galleries.GalleryImage')),
                ('event_date', models.DateField(blank=True, null=True, verbose_name='\u884c\u4e8b\u65e5')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('galleries.galleryimage',),
        ),
        migrations.AddField(
            model_name='galleryimageextra',
            name='detail',
            field=models.CharField(blank=True, max_length=1000, verbose_name='\u8a73\u7d30'),
        ),
    ]
