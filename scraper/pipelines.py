# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CombinePipeline(object):
	
	def __init__(self):
		self.file=open('items.jl','wb')
	def process_item(self, item, spider):
		if item['videolinks']:
			line=json.dumps(dict(item)['videolinks'][0])+"\n"
			self.file.write(line)
			return item
