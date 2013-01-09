from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

from favorites.urls import FavoritesPublic
from favorites.urls import FavoritesPrivate

from favorites.models import Favorite


staff_favorites = Favorite.objects.all().filter(user__is_staff=True)


urlpatterns = patterns('',
    url('^$', TemplateView.as_view(template_name='main/index.html')),
    url('^', FavoritesPublic('favorites-all').include_urls()),
    url('^staff/favorites/', FavoritesPublic('favorites-staff', staff_favorites).include_urls()),
    url('^my/favorites/', FavoritesPrivate().include_urls()),
)
