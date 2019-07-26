# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import pymongo
from bson import json_util

from scrapy.conf import settings
import json

class DogbrainspiderPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host=host,port=port)
        mdb = client[dbname]

        self.post = mdb['news']

    def open_spider(self, spider):

        print("开始爬虫")

    def process_item(self, item, spider):


        data = dict(item)
        # self.post.insert(data)
        self.post.update({"full_url": data['full_url']}, {"$set":data}, True)

        return item

    def close_spider(self, spider):
        print("结束爬虫")

        msgs = self.post.find({})
        json_docs = []

        for msg in msgs:
            json_doc = json.dumps(msg, default=json_util.default)
            json_docs.append(json_doc)

        # print(json_docs)