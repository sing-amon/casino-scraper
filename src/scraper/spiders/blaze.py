import scrapy


class BlazeSpider(scrapy.Spider):
    name = "blaze"
    allowed_domains = ["blaze.bet.br"]
    start_urls = ["https://blaze.bet.br/pt/casino"]

    def parse(self, response):
        pass
