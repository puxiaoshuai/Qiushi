# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  sqlalchemy.orm import sessionmaker
from  Qiushi.models import engine,QushiBean
class QiushiPipeline(object):
    def process_item(self, item, spider):
        self.session.add(QushiBean(**item))
        return item
    def open_spider(self,item):
        Seesi=sessionmaker(bind=engine)
        self.session=Seesi()
        print("start---")
    def close_spider(self,item):
        self.session.commit()
        self.session.close()
        print("end----")
