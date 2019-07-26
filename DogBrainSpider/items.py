# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DogbrainspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    full_url = scrapy.Field()
    media = scrapy.Field()
    media_url = scrapy.Field()

    pass
