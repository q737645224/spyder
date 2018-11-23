# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #抓取招聘职位的名称,链接及类型
    positionName = scrapy.Field() 
    positionLink = scrapy.Field()
    positionType = scrapy.Field()
