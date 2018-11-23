# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tencent2Spider(CrawlSpider):
    name = 'tencent2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/']

    # 这个rules使得CrawlSpider可以更加灵活的获取url信息
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
