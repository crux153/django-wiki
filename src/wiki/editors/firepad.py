from django import forms
from django.conf import settings as django_settings
from wiki.editors.base import BaseEditor


class FirepadWidget(forms.Widget):
    template_name = "wiki/forms/firepad.html"

    def __init__(self, attrs=None):
        # The 'rows' and 'cols' attributes are required for HTML correctness.
        default_attrs = {
            "id": "firepad"
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["firebase"] = {
            "apiKey": getattr(django_settings, "FIREBASE_API_KEY"),
            "authDomain": getattr(django_settings, "FIREBASE_AUTH_DOMAIN"),
            "databaseURL": getattr(django_settings, "FIREBASE_DATABASE_URL"),
        }
        return context


class Firepad(BaseEditor):
    editor_id = "firepad"

    def get_admin_widget(self, instance=None):
        return FirepadWidget()

    def get_widget(self, instance=None):
        return FirepadWidget()

    class AdminMedia:
        css = {
            "all": ()
        }
        js = ()

    class Media:
        css = {
            "all": (
                "wiki/firepad/codemirror.css",
                "wiki/firepad/firepad.css",
                "wiki/firepad/firepad.theme.css",
            )
        }
        js = (
            "wiki/firepad/firebase-app.js",
            "wiki/firepad/firebase-auth.js",
            "wiki/firepad/firebase-database.js",
            "wiki/firepad/codemirror.js",
            "wiki/firepad/codemirror-markdown.js",
            "wiki/firepad/firepad.min.js",
            "wiki/firepad/firepad.init.js",
        )
