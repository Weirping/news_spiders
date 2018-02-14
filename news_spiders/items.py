# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    web_site = scrapy.Field()
    web_title = scrapy.Field()
    web_url = scrapy.Field()
    archive_time = scrapy.Field()
