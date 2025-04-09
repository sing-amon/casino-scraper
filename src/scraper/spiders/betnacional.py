import scrapy


class BetnacionalSpider(scrapy.Spider):
    name = "betnacional"
    allowed_domains = ["betnacional.bet.br"]
    start_urls = ["https://betnacional.bet.br/casino/lobby"]

    def parse(self, response):
        pass
