from django.contrib import admin

from ..models.lists import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(List, ListAdmin)
