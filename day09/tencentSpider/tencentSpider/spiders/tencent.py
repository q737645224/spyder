# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    #start_urls = ['https://hr.tencent.com/position.php?keywords=Python&start=0#a']
#    start_urls = []
#    
#    for i in range(0, 530, 10):
#        url = 'https://hr.tencent.com/position.php?keywords=Python&start='
#        url += str(i)+"#a"
#        start_urls.append(url)
    
    url = 'https://hr.tencent.com/position.php?keywords=Python&start='
    offset = 0
    start_urls = [url+str(offset)+'#a']
                          
    def parse(self, response):
        # 提取数据
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentspiderItem()
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = 'https://hr.tencent.com/'+each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            yield item
        
        # 提取链接
        if self.offset < 530:
            self.offset += 10
            nextPageUrl = self.url+str(self.offset)+"#a"
        else:
            return
        # 对下一页发起请求
        yield scrapy.Request(nextPageUrl, callback=self.parse)
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
