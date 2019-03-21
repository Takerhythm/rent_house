# -*- coding: utf-8 -*-
import scrapy


class RentHouseSpider(scrapy.Spider):
    name = 'rent_house'
    allowed_domains = ['ab.lianjia.com']
    start_urls = ['http://ab.lianjia.com/']

    def parse(self, response):
        pass
