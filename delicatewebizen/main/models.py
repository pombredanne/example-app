from django.db import models
from django.http import HttpResponse
from django.template.response import SimpleTemplateResponse


from favorites.utils import BaseRender
from favorites.utils import ModelRenderMixin


class Link(models.Model, ModelRenderMixin):
    title = models.CharField(max_length=255)
    url = models.URLField()

    class Render(BaseRender):

        def full(self):
            return self.render('main/link/full.html')

        def preview(self):
            return self.render('main/link/preview.html')

        def inline(self):
            return self.render('main/link/inline.html')

    def __str__(self):
        return self.title


class Poem(models.Model, ModelRenderMixin):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

    class Render(BaseRender):

        def full(self):
            return self.render('main/poem/full.html')

        def preview(self):
            return self.render('main/poem/preview.html')

        def inline(self):
            return self.render('main/poem/inline.html')

    def __str__(self):
        return '%s by %s' % (self.title, self.author)
