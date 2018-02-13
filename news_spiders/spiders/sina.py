# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class SinaSpider(HomepageSpider):
    name = u"sina"
    allowed_domains = [u"sina.com.cn"]
    start_urls = [u'http://www.sina.com.cn/']
