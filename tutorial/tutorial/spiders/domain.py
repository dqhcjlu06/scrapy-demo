# -*- coding: utf-8 -*-
import scrapy


class DomainSpider(scrapy.Spider):
    name = 'domain'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
