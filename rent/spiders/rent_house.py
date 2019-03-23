# -*- coding: utf-8 -*-
import json

import scrapy


class RentHouseSpider(scrapy.Spider):
    name = 'rent_house'
    allowed_domains = ['lianjia.com']
    base_url = r'https://app.api.lianjia.com/Rentplat/v1/house/list?city_id=440300&offset=%s&limit=30&scene=home'
    start_urls = ['https://app.api.lianjia.com/Rentplat/v1/house/list?city_id=440300&offset=0&limit=30&scene=home']
    page = 0
    def parse(self, response):
        # with open('lianjia.json', 'wb') as f:
        #     f.write(response.body)
        houses_data = json.loads(response.body.decode())
        for house_data in houses_data['data']['list']:
            house_url = house_data['m_url']
            item = {'url': house_url}
            item['house_addr'] = house_data['resblock_name']
            yield item
        print('*'* 100)
        if len(houses_data['data']['list']) < 30:
            return
        self.page += 1
        url = self.base_url % (self.page * 30)
        print(url)
        yield scrapy.Request(url, callback=self.parse)
    #
    # def parse_house(self, response):
    #     item = response.meta['house']
    #     house_center = response.xpath('//div[@class="box page-map-main"]//img/@data-src').extract_first()
    #     item['house_location'] = house_center[int(house_center.find('='))+1: int(house_center.find('&'))]
    #     item["house_price"] = response.xpath('//ul[@class="page-house-rent-list"]//div[@class="text"]/strong/text()').extract()
    #     item['house_name'] = response.xpath("//div[@class='box brand-link']//p/text()").extract_first().strip()
    #     item['house_addr'] = response.xpath("//div[@class='box page-map-main']//p[@class='flat_detail--address oneline']/text()").extract_first()
    #     yield item