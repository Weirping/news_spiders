# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

class IfengHomepageSpider(scrapy.Spider):
    name = "ifeng_homepage"
    allowed_domains = ["ifeng.com"]
    start_urls = ['http://www.ifeng.com/']

    def parse(self, response):
        logger.info(u'response status :' + unicode(response.status))
        areaDefault_node = response.xpath(u'//*[@id="headLineDefault"]')
        for t, a in self.area_xpath(areaDefault_node):
            print t, a



    def area_xpath(self, areaDefault_node):
        hrefs = areaDefault_node.xpath(u'//ul[@class="FNewMTopLis"]//a/@href').extract()
        titles = areaDefault_node.xpath(u'//ul[@class="FNewMTopLis"]//a/text()').extract()
        logger.info(u'hres len: ' + unicode(len(hrefs)))
        logger.info(u'titles len: ' + unicode(len(titles)))
        for i in range(0, len(titles)):
            yield titles[i].strip(), hrefs[i].strip()
