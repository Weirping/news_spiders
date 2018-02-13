# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from homepage import HomepageSpider
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)


class YouthSpider(HomepageSpider):
    name = u"youth"
    allowed_domains = [u"youth.cn"]
    start_urls = [u'http://www.youth.cn/']
