# -*- coding: utf-8 -*-
import os
import sys
import logging
import scrapy
from news_spiders.items import NewsSpidersItem
import datetime
reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

class HomepageSpider(scrapy.Spider):
    '''
    通过当前实验,所有网站的首页都可以用如下逻辑解析出title和url,所以将homepage的抓取逻辑设计成了各门户网站抓取逻辑的积累
    在各子类中重新定义 name allowed_domains start_urls 就可以直接抓取homepage

    '''
    name = None
    allowed_domains = [u""]
    start_urls = [u'']

    def parse(self, response):
        logger.info(self.name + u'response status :' + unicode(response.status))
        a_index = 1
        titles, hrefs = self._get_titles_hrefs(a_index, response)
        while len(titles) > 0:
            if len(titles) != len(hrefs):
                logger.warn(u'len(titles) != len(hrefs)')
                a_index +=1
                continue
            for i in xrange(0, len(titles)):
                nsi = NewsSpidersItem()
                nsi[u'web_site'] = self.name
                nsi[u'web_title'] = titles[i].strip()
                nsi[u'web_url'] = hrefs[i].strip()
                nsi[u'archive_time'] = datetime.datetime.now().strftime(u'%Y-%m-%d %H:%M:%S')
                yield nsi
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
