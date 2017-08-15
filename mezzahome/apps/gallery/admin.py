# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import GalleryImageExtra


class GalleryImageExtraInline(admin.TabularInline):
    verbose_name_plural = ('GalleryImageExtra')
    model = GalleryImageExtra
    extra = 0
