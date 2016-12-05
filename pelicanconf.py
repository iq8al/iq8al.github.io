#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '.'))

AUTHOR = 'Iqbal Abdullah'
SITENAME = "iqbalabd's blog on the internet"
TOP_PAGE_TITLE = "Blog Top"
SITEURL = 'http://localhost:8000'
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
            ('linkedin', 'https://www.linkedin.com/in/iqbalabd'),
            ('github', 'https://github.com/iq8al'),
            ('twitter', 'https://twitter.com/iqbalabd'),
         )

DEFAULT_PAGINATION = 10

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME           = 'themes/pelican-blue'
PLUGIN_PATHS    = [os.path.join(PROJECT_ROOT, 'plugins'),]
PLUGINS         = ["i18n_subsites", ]

I18N_UNTRANSLATED_ARTICLES  = "keep"
I18N_UNTRANSLATED_PAGES     = "keep"

I18N_SUBSITES   = {
    'ja': {
        'SITENAME': 'Iqbal, Rileks La.',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
        'TOP_PAGE_TITLE': TOP_PAGE_TITLE,
    },
    'ms': {
        'SITENAME': 'Iqbal, Rileks La.',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
        'TOP_PAGE_TITLE': TOP_PAGE_TITLE,
    },
    'en': {
        'SITENAME': 'Iqbal, Rileks La.',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
        'TOP_PAGE_TITLE': TOP_PAGE_TITLE,
    },
}

languages_lookup = {
    'en': 'English',
    'ja': '日本語',
    'ms': 'Bahasa Kebangsaan',
}

# pelican-blue theme settings
SIDEBAR_DIGEST = 'またのブログ'
#FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'iqbalabd'
MENUITEMS = (
    ('Blog Top', SITEURL),
    ('Xoxzo Inc.', 'https://info.xoxzo.com/'),
)
DISPLAY_SUMMARY = True

