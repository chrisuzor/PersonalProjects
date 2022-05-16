# timeline/admin.py
from django.contrib import admin

from .models import Entry, Timeline


@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "length", "rank")
