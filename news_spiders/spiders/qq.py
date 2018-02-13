# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class QqSpider(HomepageSpider):
    name = u"qq"
    allowed_domains = [u"qq.com"]
    start_urls = [u'http://www.qq.com/']
