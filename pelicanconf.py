#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Carlos Carvalho'
SITENAME = 'Carlos Carvalho'
SITEURL = 'http://chcdc.com.br/'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
SUMMARY_MAX_LENGTH = 50


# Github Profile
GITHUB_URL = 'http://github.com/chcdc/'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_USE_SUMMARY = True


# Paths
PATH = 'content'

ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

STATIC_PATHS = [
        'themes',
        'images',
        'extra/robots.txt',
        'extra/favicon.ico',
        'extra/CNAME'
        ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

PLUGIN_PATH = './.plugins'
PLUGINS = [
        'gzip_cache',
        'pelican_gist',
        'related_posts',
        'summary',
        'optimize_images',
        'sitemap',
        'post_stats',
        'share_post',
        ]


# Path THEME
THEME = './themes/genus' 


# Theme customizations
GRAVATAR_IMAGE = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
SITETITLE = 'Carlos Carvalho'
#SITESUBTITLE = 'Tste'

SUMMARY_END_MARKER = '<!--more-->'

PAGINATION_PATTERNS = (
        (1, '{base_name}/', '{base_name}/index.html'),
        (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
        )


# Blogroll
#LINKS = (('Pelican', 'http://gepelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = 'True'
# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = 'True'
# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = 'True'

# Social widget
SOCIAL = (
        ('github', 'https://github.com/chcdc'),
#        ('twitter', 'https://twitter.com/chcdc'),
#        ('google+', 'http://plus.google.com/102063745956138544914'),
#        ('facebook', 'http://facebook.com/MindBendingBlog'),
#        ('stack-overflow', 'http://stackoverflow.com/users/498227'),
#        ('gittip', 'https://www.gittip.com/magnunleno/'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

