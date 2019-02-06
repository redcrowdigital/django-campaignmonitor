from django.db import models
from django.utils.translation import ugettext_lazy as _
from .lists import List

STATE_ACTIVE = 1
STATE_INACTIVE = 2


class Subscriber(models.Model):
    STATE_CHOICES = (
        (STATE_ACTIVE, _("active")),
        (STATE_INACTIVE, _("inactive")),
    )
    
    email_address = models.CharField(verbose_name=_("email address"), max_length=200)
    name = models.CharField(verbose_name=_("name"), max_length=200)
    date = models.DateTimeField(verbose_name=_("date")),
    state = models.PositiveIntegerField(verbose_name=_("state"), choices=STATE_CHOICES)
    list = models.ForeignKey(List)

    class Meta:
        verbose_name = _("subscriber")
        verbose_name_plural = _("subscribers")
        app_label = 'campaignmonitor'

    def __str__(self):
        return self.email_address


class SubscriberCustomField(models.Model):
    subscriber = models.ForeignKey(Subscriber, verbose_name=_("subscriber"), related_name='custom_fields')
    key = models.CharField(verbose_name=_("key"), max_length=127)
    value = models.CharField(verbose_name=_("value"), max_length=255)
    
    class Meta:
        verbose_name = _("custom field")
        verbose_name_plural = _("custom fields")
        app_label = 'campaignmonitor'
