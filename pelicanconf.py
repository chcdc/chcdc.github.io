#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Carlos Carvalho'
SITENAME = 'Carlos Carvalho'
SITETITLE = 'Carlos Carvalho'
SITEURL = 'http://chcdc.com.br/'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt'
OG_LOCALE = 'pt_BR'
DEFAULT_CATEGORY = 'misc'
DELETE_OUTPUT_DIRECTORY = True
MAIN_MENU = True
DEFAULT_PAGINATION = 10
SUMMARY_END_MARKER = '<!--more-->'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_USE_SUMMARY = True

# Github Profile
GITHUB_URL = 'http://github.com/chcdc/'


# Disqus
DISQUS_SITENAME = "chcdc"

# Path THEME
THEME = './themes/Flex/'
#THEME = './themes/genus/'

# Google AdSense
"""GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-4103262705608837',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'main_menu': '1234562',      # Banner before main menu (all pages)
        'index_top': '1234563',      # Banner after main menu (index only)
        'index_bottom': '1234564',   # Banner before footer (index only)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
"""
# Google Analytics
GOOGLE_ANALYTICS = 'UA-66134049-1'

# Theme customizations
GRAVATAR_IMAGE = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
PYGMENTS_STYLE = 'solarized-dark'
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
USE_LESS = True
# Social widget
SOCIAL = (
        ('github', 'https://github.com/chcdc'),
        ('stack-overflow', 'https://pt.stackoverflow.com/users/26828'),
        ('rss', 'http://chcdc.com.br/feeds/all-pt.atom.xml'),
        ('twitter', 'https://twitter.com/chcdc'),
        ('linkedin', 'https://www.linkedin.com/in/chcdc/'),
        ('telegram', 'http://telegram.me/chcdc'),
        )
#LINKS = (('About me', 'http://alexandrevicenzi.com'),)
DEFAULT_METADATA = {
            'status': 'draft',
            }


# Paths
PATH = 'content'
RELATIVE_URLS = True

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

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


PAGINATION_PATTERNS = (
        (1, '{base_name}/', '{base_name}/index.html'),
        (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
        )

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
