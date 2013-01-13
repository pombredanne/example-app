from django.contrib import admin as djangoadmin

import compositeadmin

from .models import Favorite


for admin in (compositeadmin, djangoadmin):

    class FavoriteAdmin(admin.ModelAdmin):
        list_display = ('object', 'user', 'content_type',)
        list_filter = ('content_type', )

    admin.site.register(Favorite, FavoriteAdmin)
