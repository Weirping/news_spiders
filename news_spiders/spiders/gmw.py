# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class GmwSpider(HomepageSpider):
    name = u"gmw"
    allowed_domains = [u"gmw.cn"]
    start_urls = [u'http://www.gmw.cn/']
