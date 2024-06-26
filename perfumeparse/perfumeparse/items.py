import scrapy


class PerfumeparseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    valume = scrapy.Field()
    image = scrapy.Field()
    type = scrapy.Field()
    aromas = scrapy.Field()
    url = scrapy.Field()