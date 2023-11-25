import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://example.com']

    def parse(self, response):
        for href in response.css('a::attr(href)'):
            yield {'link': href.get()}

# To run the spider, use the command: scrapy runspider my_spider.py
