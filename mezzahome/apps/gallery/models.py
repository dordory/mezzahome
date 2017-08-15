# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class GalleryImageExtra(models.Model):
    image = models.OneToOneField('galleries.GalleryImage', related_name='extra')
    event_date = models.DateField('行事日', blank=True, null=True)
