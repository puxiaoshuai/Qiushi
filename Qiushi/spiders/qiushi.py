# -*- coding: utf-8 -*-
import scrapy


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ("https://www.qiushibaike.com/pic/page/{}/".format(i)  for i in range(1,41))

    def parse(self, response):
        pass
