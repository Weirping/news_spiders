# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class PeopleSpider(HomepageSpider):
    name = u"people"
    allowed_domains = [u"people.com.cn"]
    start_urls = [u'http://www.people.com.cn/']
