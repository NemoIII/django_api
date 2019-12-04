from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class PostUpdate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timastamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
    