# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.galleries.admin import GalleryAdmin, GalleryImageInline

from models import GalleryImageExtra, ExtendGalleryImage


@admin.register(ExtendGalleryImage)
class ExtendGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'gallery', 'file', 'description', 'event_date', )
