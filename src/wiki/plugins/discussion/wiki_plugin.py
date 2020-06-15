from django.utils.translation import gettext as _
from wiki.core.plugins import registry
from wiki.core.plugins.base import BasePlugin


class DiscussionPlugin(BasePlugin):

    slug = "discussion"

    sidebar = {
        "headline": _("Discussion"),
        "icon_class": "fa-comments",
        "template": "wiki/plugins/discussion/sidebar.html",
        "form_class": None,
        "get_form_kwargs": (lambda a: {}),
    }

    class RenderMedia:
        js = [
            "wiki/firechat/firechat.min.js",
        ]

        css = {"screen": "wiki/firechat/firechat.min.css"}

    markdown_extensions = []


registry.register(DiscussionPlugin)
