# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider

reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class XinhuaSpider(HomepageSpider):
    name = u"xinhua"
    allowed_domains = [u"xinhuanet.com"]
    start_urls = [u'http://www.xinhuanet.com/']
