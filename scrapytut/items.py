# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    crawlingpage_name = scrapy.Field()
    crawlingpage_address = scrapy.Field()
    crawlingpage_ratings = scrapy.Field()
    crawlingpage_reviews = scrapy.Field()

