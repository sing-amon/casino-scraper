import scrapy


class BetanoSpider(scrapy.Spider):
    name = "betano"
    allowed_domains = ["www.betano.bet.br"]
    start_urls = ["https://www.betano.bet.br/casino/"]

    def parse(self, response):
        pass
