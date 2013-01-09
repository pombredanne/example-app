from django.contrib import admin

from .models import Favorite


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('object', 'user')
    list_filter = ('content_type', )

admin.site.register(Favorite, FavoriteAdmin)
