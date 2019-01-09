# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderEbayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()


class EbayItems(scrapy.Item):

    link = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    desc = scrapy.Field()
    type = scrapy.Field()
    is_shipping = scrapy.Field()
