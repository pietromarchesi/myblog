#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pietro Marchesi'
SITENAME = u'Pietro Marchesi'
SITEURL = 'http://pietromarchesi.net'
SITETITLE = 'Pietro Marchesi'
SITELOGO = SITEURL + '/images/profile1.jpg'
SITEURL = 'pietromarchesi.net'
RELATIVE_URLS = True


MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"] 

PATH = 'content'
STATIC_PATHS = ['images']

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'),)

THEME = "/home/pietro/pelican-themes/Flex"
TIMEZONE = 'Europe/Paris'
SIDEBAR_DISPLAY = ['about', 'categories']
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
COPYRIGHT = "Pietro Marchesi "


DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('pietro\'s data bulletin', '/category/pietros-data-bulletin.html'),
         ('tutorials', '/category/tutorials.html'),
	 ('some other stuff', '/category/some-other-stuff.html'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/pietro_marchesi'),
          ('github', 'https://github.com/pietromarchesi'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
