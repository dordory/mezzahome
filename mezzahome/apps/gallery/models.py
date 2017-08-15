# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mezzanine.galleries.models import Gallery, GalleryImage


class GalleryImageExtra(models.Model):
    image = models.OneToOneField('galleries.GalleryImage', related_name='extra')
    event_date = models.DateField('行事日', blank=True, null=True)
    detail = models.CharField("詳細", max_length=1000, blank=True)


class ExtendGalleryImage(GalleryImage):
    event_date = models.DateField('行事日', blank=True, null=True)
