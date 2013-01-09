from django.views.generic import DetailView

from composite import StackedCompositeView
from composite import SortableTable
from composite import Filter
from composite.mixin import LoginRequiredMixin

from .models import Favorite


def title(obj):
    return obj.object.render.inline()
title.verbose_name = ''


class ListView(StackedCompositeView):

    list_display = (title, 'content_type', 'user')
    list_filter = ('content_type',)

    template_name = 'favorites/list.html'
    queryset = None

    def _queryset(self, request, *args, **kwargs):
        return self.queryset

    def _composites(self, request, *args, **kwargs):
        options = dict(
            list_filter=self.list_filter,
            model_class=Favorite,
            parent=self,
        )
        filter = Filter(**options)
        # filter is used before it has been init for this request
        # and it expects request to be available
        filter.request = self.request
        options = dict(
            queryset=self._queryset(request),
            model_class=Favorite,
            filter=filter,
            parent=self,
            list_display=self.list_display,
        )
        table = SortableTable(**options)
        yield table
        yield filter


class UserListView(ListView, LoginRequiredMixin):

    list_display = (title, 'content_type', 'user')
    list_filter = ('content_type',)

    template_name = 'favorites/list.html'

    def _queryset(self, request, *args, **kwargs):
        qs = super(UserListView, self)._queryset(request, *args, **kwargs)
        if not qs:
            qs = Favorite.objects.all().filter(user=request.user)
        return qs.filter(user=request.user)
