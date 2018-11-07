# -*- coding: utf-8 -*-
import scrapy

from Qiushi.items import QiushiItem


class BudejieSpider(scrapy.Spider):
    name = 'budejie'
    allowed_domains = ['budejie.com']
    start_urls = ("http://www.budejie.com/pic/{}".format(i) for i in range(1, 2))

    def parse(self, response):

        for article in  response.xpath('//div[@class="j-r-list"]/ul/li'):
            cont= article.xpath('.//div[@class="j-r-list-c-desc"]/a/text()').re(r'(\w+)')
            data=",".join(cont)
            item=QiushiItem({
                'name':article.xpath('.//div[@class="u-txt"]/a/text()').extract_first(),
                'content':data,
                'image_url':article.xpath('.//div[@class="j-r-list-c-img"]/a/img/@data-original').extract_first()
            })
            yield item



