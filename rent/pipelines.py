# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class RentPipeline(object):
    def open_spider(self, spider):
        self.file = open('../lianjia.csv', 'wb')
        self.writer = CsvItemExporter(self.file)
        self.writer.start_exporting()

    def process_item(self, item, spider):
        self.writer.export_item(item)
        return item

    def close_spider(self, response):
        self.writer.finish_exporting()
        self.file.close()