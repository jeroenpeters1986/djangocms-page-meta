# -*- coding: utf-8 -*-
from aldryn_client import forms


OBJECT_TYPES = (
    ('Article', 'Article'),
    ('Website', 'Website'),
)

PROTOCOLS = (
    ('http', 'http'),
    ('https', 'https'),
)


class Form(forms.BaseForm):

    META_SITE_PROTOCOL = forms.SelectField(
        'META_SITE_PROTOCOL',
        choices=PROTOCOLS
    )
    META_SITE_TYPE = forms.SelectField(
        'META_SITE_TYPE',
        choices=OBJECT_TYPES
    )
    META_SITE_NAME = forms.CharField('META_SITE_NAME', required=False)
    META_IMAGE_URL = forms.CharField('META_IMAGE_URL', required=False)
    META_USE_OG_PROPERTIES = forms.CheckboxField(
        'META_USE_OG_PROPERTIES',
        required=False
    )
    META_USE_TWITTER_PROPERTIES = forms.CheckboxField(
        'META_USE_TWITTER_PROPERTIES',
        required=False
    )
    META_USE_GOOGLEPLUS_PROPERTIES = forms.CheckboxField(
        'META_USE_GOOGLEPLUS_PROPERTIES',
        required=False
    )

    def to_settings(self, data, settings):
        settings['META_SITE_PROTOCOL'] = data['META_SITE_PROTOCOL']
        settings['META_SITE_TYPE'] = data['META_SITE_TYPE']
        settings['META_SITE_NAME'] = data['META_SITE_NAME']
        settings['META_INCLUDE_KEYWORDS'] = []
        settings['META_DEFAULT_KEYWORDS'] = []
        settings['META_IMAGE_URL'] = data['META_IMAGE_URL']
        settings['META_USE_OG_PROPERTIES'] = data['META_USE_OG_PROPERTIES']
        settings['META_USE_TWITTER_PROPERTIES'] = data['META_USE_TWITTER_PROPERTIES']
        settings['META_USE_GOOGLEPLUS_PROPERTIES'] = data['META_USE_GOOGLEPLUS_PROPERTIES']
        settings['META_USE_TITLE_TAG'] = False
        settings['META_USE_SITES'] = True
        return settings