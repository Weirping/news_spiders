# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class CeSpider(HomepageSpider):
    name = u"ce"
    allowed_domains = [u"ce.cn"]
    start_urls = [u'http://www.ce.cn/']
