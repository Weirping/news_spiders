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
        a_index = 1
        titles, hrefs = self._get_titles_hrefs(a_index, response)
        while len(titles) > 0:
            if len(titles) != len(hrefs):
                logger.warn(u'len(titles) != len(hrefs)')
                a_index +=1
                continue
            for i in xrange(0, len(titles)):
                pass
                # print titles[i].strip(), hrefs[i].strip()
            a_index += 1
            titles, hrefs = self._get_titles_hrefs(a_index, response)

    def _get_titles_hrefs(self, a_index, response):
        def th_xpath(i):
            return u"//a[count(*)=0 and @href and string-length(text())>2 and starts-with(@href, 'http')][%d]/text()" %i, \
                    u"//a[count(*)=0 and @href and string-length(text())>2 and starts-with(@href, 'http')][%d]/@href" %i
        t_xpath, h_xpath = th_xpath(a_index)
        titles = response.xpath(t_xpath).extract()
        hrefs = response.xpath(h_xpath).extract()
        return titles, hrefs
