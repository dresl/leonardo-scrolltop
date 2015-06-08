
from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget


class ScrollTopWidget(Widget):

    duration = models.PositiveIntegerField(verbose_name=_("duration"), default=300)

    class Meta:
        abstract = True
        verbose_name = _("scroll top")
        verbose_name_plural = _('scroll top widgets')
