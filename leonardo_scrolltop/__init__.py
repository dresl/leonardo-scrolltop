
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'leonardo_scrolltop.Config'

try:
    from local_settings import APPS
except ImportError:
    pass

class Default(object):

    optgroup = 'Common'

    if 'leonardo_scrolltop' in APPS:
        apps = [
            'leonardo_scrolltop'
        ]

        css_files = [
            'scrolltop/default.css'
        ]

        widgets = [
            'leonardo_scrolltop.widget.scrolltop.models.ScrollTopWidget'
        ]

class Config(AppConfig, Default):
    name = 'leonardo_scrolltop'
    verbose_name = _("ScrollTop")

default = Default()
