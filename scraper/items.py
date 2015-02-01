from scrapy.item import Item, Field

class ScraperItems(Item):
    url=Field()

    videolinks=Field()
   
