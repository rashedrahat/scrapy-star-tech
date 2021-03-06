# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StarTechItem(scrapy.Item):
    # define the fields for your item here like:
    gadget_name = scrapy.Field()
    gadget_model = scrapy.Field()
    gadget_category = scrapy.Field()
    gadget_brand = scrapy.Field()
    gadget_price = scrapy.Field()
    gadget_specification = scrapy.Field()
    gadget_img_url = scrapy.Field()
    e_commerce_website = scrapy.Field()
    gadget_url = scrapy.Field()
