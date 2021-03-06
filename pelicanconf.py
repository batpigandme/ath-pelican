#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site development flag
developing_site = True
# DELETE_OUTPUT_DIRECTORY = True

# ------------------
# Site information
# ------------------
AUTHOR = 'Andrew Heiss'
SITENAME = 'Andrew Heiss'
MINIBIO = 'International NGOs, nonprofit management, authoritarianism, data visualization, and R'
DESCRIPTION = 'Andrew Heiss is a visiting assistant professor at the Romney Institute of Public Management at Brigham Young University, researching international NGOs in authoritarian regimes and teaching data visualization and economics.'

SITEURL = ''
DEFAULT_SOCIAL_IMG = SITEURL + '/theme/img/meta_img.png'

TIMEZONE = 'America/Denver'
DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%A, %B %-d, %Y'

TYPOGRIFY = True  # Nice typographic things

GOOGLE_ANALYTICS = ''


# ---------------
# Site building
# ---------------
# Theme
THEME = 'theme'

# Folder where everything lives
PATH = 'content'

# Structure of output folder
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

INDEX_SAVE_AS = 'blog/index.html'

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = 'blog/categories/index.html'

TAG_SAVE_AS = ''
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_SAVE_AS = ''

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

# Get rid of author pages (since I'm the only author) and the archives page
# (since I'm doing that manually)
DIRECT_TEMPLATES = ('index', 'categories', 'tags')

# Include source files, just for fun
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.txt'

# Ordering
PAGE_ORDER_BY = 'date'
ARTICLE_ORDER_BY = 'reversed-date'

STATIC_PATHS = ['files', 'keybase.txt']
READERS = {'html': None}  # Don't parse HTML files

TEMPLATE_PAGES = {'feed.json': 'feed.json'}


# ---------
# Plugins
# ---------
PLUGIN_PATHS = ['/Users/andrew/Sites/Pelican/pelican-plugins']
PLUGINS = ['collate_content', 'sitemap', 'dateish']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.smarty': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'baselevel': 1},
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.headerid': {'level': 2}
    },
    'output_format': 'html5',
}

# collate_content settings
# CATEGORIES_TO_COLLATE = ['category-of-interest', 'another-cool-category']

# Sitemap settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'weekly'
    }
}

# dateish settings
# DATEISH_PROPERTIES = ['created_date', 'idea_date']


# Feed generation
FEED_ALL_ATOM = None if developing_site else 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Cache
LOAD_CONTENT_CACHE = False if developing_site else True


# ------------
# Site items
# ------------
MENUITEMS = [('About', '/'), ('CV', '/files/2017-09-22-andrew-heiss-cv.pdf'),
             ('Blog', '/blog/'), ('Research', '/research/'),
             ('Notebook', 'https://notebook.andrewheiss.com/'),
             ('Teaching', '/teaching/'),
             ('Other projects', '/other-projects/'),
             ('Now', '/now/'), ('Uses', '/uses/')]

SOCIAL = [('E-mail', 'mailto:andrew@andrewheiss.com', 'fa-envelope-square'),
          ('Heissatopia (family blog)', 'http://www.heissatopia.com', 'fa-smile-o'),
          ('Facebook', 'https://www.facebook.com/andrewheiss', 'fa-facebook-square'),
          ('Twitter', 'https://twitter.com/andrewheiss', 'fa-twitter-square'),
          ('GitHub', 'https://github.com/andrewheiss', 'fa-github-square'),
          ('StackOverflow', 'https://stackoverflow.com/users/120898/andrew', 'fa-stack-overflow'),
          ('LinkedIn', 'https://www.linkedin.com/in/andrewheiss', 'fa-linkedin-square')]


# ---------------
# Jinja filters
# ---------------
import jinja2
import markdown
from bs4 import BeautifulSoup

# Remove <p>s surrounding Markdown output
def md_single_line(text):
    p = '<p>'
    np = '</p>'
    md = markdown.markdown(text)
    if md.startswith(p) and md.endswith(np):
        md = md[len(p):-len(np)]
    return jinja2.Markup(md)

def md(text):
    return jinja2.Markup(markdown.markdown(text))

def pure_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    for table_tag in soup.find_all('table'):
        table_tag['class'] = table_tag.get('class', []) + ['pure-table']

    return jinja2.Markup(soup)

def fmt_date(value, fmt):
    return value.strftime(fmt)

def current_year(value):
    import time
    return(time.strftime("%Y"))

def jsonify(text):
    import json
    return json.dumps(text, ensure_ascii=False)

def titlify(text):
    soup_title = BeautifulSoup(text.replace('&nbsp;', ' '), 'html.parser')
    page_title = soup_title.get_text(' ', strip=True)
    return(page_title)


JINJA_FILTERS = {'md_single_line': md_single_line,
                 'md': md,
                 'pure_table': pure_table,
                 'fmt_date': fmt_date,
                 'current_year': current_year,
                 'jsonify': jsonify,
                 'titlify': titlify}


# ----------------------------
# Other filters and snippets
# ----------------------------
# Make PHP snippets highlight without <?php
import pygments.lexers.web as pygweb
class MyPhpLexer(pygweb.PhpLexer):
    def __init__(self, **options):
        options['_startinline'] = True
        super().__init__(**options)
pygweb.PhpLexer = MyPhpLexer
