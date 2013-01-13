from composite import UrlCollection

from .views import ListView
from .views import UserListView


class FavoritesPublic(UrlCollection):

    application_namespace = 'favorites-public'

    def __init__(self, instance_namespace=None, queryset=None):
        super(FavoritesPublic, self).__init__(instance_namespace)
        self.add_url(r'^all/$', ListView, dict(queryset=queryset), 'all')


class FavoritesPrivate(UrlCollection):

    application_namespace = 'favorites-private'

    def __init__(self, instance_namespace=None):
        super(FavoritesPrivate, self).__init__(instance_namespace)
        self.add_url(r'^all/$', UserListView, name='all')
