#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Carlos Carvalho'
SITENAME = 'Carlos Carvalho'
SITEURL = 'https://blog.chcdc.com.br/'
SITEURL_ABS = SITEURL

# Biography
BIO = "Sysadmin and DevOps | More Ops than Dev"

# Theme customizations
SITETITLE = 'Carlos Carvalho'
SITESUBTITLE  = 'Yet Another Blog'
SITEDESCRIPTION = 'Yet Another Blog'

REL_CANONICAL = True
DISABLE_URL_HASH = True
ROBOTS = "index, follow"

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Carlos Carvalho"

MAIN_MENU = True
USE_GOOGLE_FONTS = True

FAVICON = SITEURL + "extra/favicon.ico"
THEME_COLOR = 'light'

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE = 'monokai'

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

## Theme Social widget
SOCIAL = (
        ('github', 'https://github.com/chcdc'),
        ('stack-overflow', 'https://pt.stackoverflow.com/users/26828'),
        ('rss', 'http://blog.chcdc.com.br/feeds/all-pt.atom.xml'),
        ('linkedin', 'https://www.linkedin.com/in/chcdc/'),
        )

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'

DEFAULT_CATEGORY = 'misc'
OUTPUT_PATH = 'output/'


DELETE_OUTPUT_DIRECTORY = True
DEFAULT_PAGINATION = 10

NEWEST_FIRST_ARCHIVES = True

SUMMARY_MAX_LENGTH = 35
SUMMARY_END_SUFFIX = '<!--more-->'
#SUMMARY_USE_FIRST_PARAGRAPH = True
#SUMMARY_END_MARKER = '<!-- PELICAN_END_SUMMARY -->'
JINJA_ENVIRONMENT  = {'extensions': ['jinja2.ext.i18n']}

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

AVATAR_USE_GRAVATAR = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
GRAVATAR_IMAGE = 'https://s.gravatar.com/avatar/b29f6fb12e1e61f1d2a46e1ec2834696?s=80'
USE_FOLDER_AS_CATEGORY = True

THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE = 'monokai'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
                'marker': '[TOC]',
                'title': 'Indice:'
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = [
        './.plugins'
        ]

PLUGINS = [
        'gzip_cache',
        'i18n_subsites',
        'neighbors',
        'pelican_gist',
        'post_stats',
        'read_more_link',
        'related_posts',
        'seo',
        'share_post',
        'sitemap',
        'summary',
        ]

# Metadata
DEFAULT_METADATA = {
            'status': 'draft',
            }

# Paths
PATH = 'content/'
# // TODO
RELATIVE_URLS = True

SLUGIFY_SOURCE = 'title'

SLUG_REGEX_SUBSTITUTIONS = [
    (r'[^\w\s-]', ''), # remove non-alphabetical/whitespace/'-' chars
    (r'(?u)\A\s*', ''), # strip leading whitespace
    (r'(?u)\s*\Z', ''), # strip trailing whitespace
    (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
]


ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

#ARTICLE_LANG_URL = '{lang}/{slug}-{lang}.html'
#ARTICLE_LANG_SAVE_AS = '{lang}/{slug}-{lang}.html'

#PAGE_URL = '{slug}/index.html'
#PAGE_SAVE_AS = '{slug}/index.html'

#PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

DRAFT_URL = 'drafts/index.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/"

AUTHOR_URL = 'author/{slug}'
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
