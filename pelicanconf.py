#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Carlos Carvalho'
SITENAME = 'Carlos Carvalho'
SITETITLE = 'Carlos Carvalho'
SITESUBTITLE  = 'Yet Another Blog'
SITEDESCRIPTION = 'Yet Another Blog'
SITEURL = 'https://blog.chcdc.com.br/'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'

DEFAULT_CATEGORY = 'misc'
OUTPUT_PATH = 'output/'
ROBOTS = "index, follow"

DELETE_OUTPUT_DIRECTORY = True
MAIN_MENU = True
DEFAULT_PAGINATION = 10

SUMMARY_END_MARKER = '<!--more-->'
JINJA_ENVIRONMENT  = {'extensions': ['jinja2.ext.i18n']}

# Biography
BIO = "Sysadmin and DevOps | More Ops than Dev"

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom'
FEED_USE_SUMMARY = True

# Github Profile
GITHUB_URL = 'http://github.com/chcdc/'

# Disqus
DISQUS_SITENAME = "chcdc"

# Path THEME
THEME = './themes/Flex/' #v2.4.0 

# Google Analytics
GOOGLE_ANALYTICS = 'UA-66134049-1'

# Theme customizations
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

FAVICON = SITEURL + "extra/favicon.ico"
AVATAR_USE_GRAVATAR = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
GRAVATAR_IMAGE = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
USE_FOLDER_AS_CATEGORY = False

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE = 'monokai'

#MARKDOWN = {
#    'extension_configs': {
#        'markdown.extensions.codehilite': {},
#        'markdown.extensions.extra': {},
#        'markdown.extensions.meta': {},
#    },
#    'output_format': 'html5',
#}

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Carlos Carvalho"

# Social widget
SOCIAL = (
        ('github', 'https://github.com/chcdc'),
        ('stack-overflow', 'https://pt.stackoverflow.com/users/26828'),
        ('rss', 'http://blog.chcdc.com.br/feeds/all-pt.atom.xml'),
        ('linkedin', 'https://www.linkedin.com/in/chcdc/'),
        )

# Metadata
DEFAULT_METADATA = {
            'status': 'draft',
            }

# Paths
PATH = 'content/'
RELATIVE_URLS = True

ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DRAFT_URL = 'drafts/index.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = 'author/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

STATIC_PATHS = [
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

PLUGIN_PATHS = [
        './.plugins'
        ]
PLUGINS = [
        'gzip_cache',
        'i18n_subsites',
        'optimize_images',
        'pelican_gist',
        'post_stats',
        'related_posts',
        'share_post',
        'sitemap',
        'summary',
        'neighbors',
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
