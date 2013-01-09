from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType



class Favorite(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = generic.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User)

    @classmethod
    def add(cls, user, object):
        favorite = cls(object=object, user=user)
        return favorite

    @classmethod
    def has(cls, user, object):
        try:
            return cls.objects.get(object=object, user=user)
        except cls.DoesNotExist:
            return False

    def __str__(self):
        return '%s favorited by %s' % (self.object, self.user)
