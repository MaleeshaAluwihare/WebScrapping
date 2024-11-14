import scrapy


class NewbookspiderSpider(scrapy.Spider):
    name = "newbookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
