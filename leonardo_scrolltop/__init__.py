
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *


default_app_config = 'leonardo_scrolltop.Config'


class Default(object):

    optgroup = 'Common'

    apps = [
        'leonardo_scrolltop'
    ]

    css_files = [
        'scrolltop/default.css'
    ]

    widgets = [
        ScrollTopWidget
    ]


class Config(AppConfig, Default):
    name = 'leonardo_scrolltop'
    verbose_name = _("ScrollTop")

default = Default()
