# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Event, Category, Assistant, Comments
from django.contrib import admin

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Assistant)
admin.site.register(Comments)
