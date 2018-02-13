# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

class IfengSpider(HomepageSpider):
    name = u"ifeng"
    allowed_domains = [u"ifeng.com"]
    start_urls = [u'http://www.ifeng.com/']
