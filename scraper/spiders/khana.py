from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from scraper.items import ScraperItems
from scrapy.http import Request

class TheSpider(CrawlSpider):
    name = 'khana'
    allowed_domains = ['fr.khanacademy.org']
    start_urls = ['https://fr.khanacademy.org']
    rules = (Rule(LxmlLinkExtractor(allow_domains=(['fr.khanacademy.org/math/','fr.khanacademy.org/science/','fr.khanacademy.org/computing/'])), callback='parse_url', follow=True), )
    def parse_url(self, response):
		item=ScraperItems()
		item['links']=response.xpath('//a[contains(@class, "topic-list-item")]/@href').extract() + response.xpath('//link[contains(@rel, "image_src")]/@href').extract()
		for i in item['links']:
			return Request(urlparse.urljoin('response.url', i[1:]))
		
	
	
		

        
