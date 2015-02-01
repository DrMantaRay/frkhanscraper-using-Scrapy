import scrapy
from scraper.items import ScraperItems
from scrapy.http import Request
from urlparse import urljoin


ilist=[]
ilist2=[]
class frspider(scrapy.Spider):
	name= 'frkhan'
	allowed_domains = ['fr.khanacademy.org']
	start_urls = ['https://fr.khanacademy.org/math/arithmetic/addition-subtraction/']
	 

	def parse(self,response):
		item=ScraperItems()
		item['url']=response.url
		ilist1=(response.xpath('//a[contains(@data-tag,"TopicBrowserPulldown")]/@href').extract()
		+response.xpath('//a[contains(@class, "topic-list-item")]/@href').extract()
		+response.xpath('//li[contains(@class,"progress-item")]/a/@href').extract())
		ilist3=response.xpath('//link[contains(@rel,"video_src")]/@href').extract()
		for i in ilist1:
			ilist2.append(urljoin('https://fr.khanacademy.org/',i[1:]))
		for i in ilist2:
			if not(i in ilist):
				ilist.append(i)
				yield Request(i)
		item['videolinks']=ilist3
		yield item
		
		
		
		
