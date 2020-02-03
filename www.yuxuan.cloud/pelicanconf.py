#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yuxuan Chen'
SITENAME = 'Yuxuan Chen'
SITEURL = 'https://www.yuxuan.cloud'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Resume', 'resume.pdf'),
         ('About', 'intro.html'),
        )
# Social widget
SOCIAL_WIDGET_NAME = 'Find me on'
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/chenyuxuan/'),
          ('GitHub', 'https://github.com/YuxuanChen'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
