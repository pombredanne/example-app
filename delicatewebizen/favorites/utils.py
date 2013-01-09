from django.template import loader
from django.template import Context
from django.utils.safestring import mark_safe
from django.db.models import get_model
from django.contrib.contenttypes.models import ContentType


def object_by_content_type(app_label, object_name, object_id):
    model = get_model(app_label, object_name)
    try:
        content_type = ContentType.objects.get_for_model(model)
    except AttributeError: # there no such model
        return None
    else:
        try:
            instance = content_type.get_object_for_this_type(pk=object_id)
        except model.DoesNotExist: # there no such object
            return None
        else:
            return instance


class ModelRenderMixin(object):

    def __init__(self, *args, **kwargs):
        super(ModelRenderMixin, self).__init__(*args, **kwargs)
        self.render = self.Render(self)


class BaseRender(object):

    def __init__(self, object):
        self.object = object

    def render(self, template):
        t = loader.get_template(template)
        c = Context(dict(object=self.object))
        r = t.render(c)
        return mark_safe(r)
