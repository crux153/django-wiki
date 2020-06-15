from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DiscussionConfig(AppConfig):
    name = "wiki.plugins.discussion"
    verbose_name = _("Wiki discussion")
    label = "discussion"
