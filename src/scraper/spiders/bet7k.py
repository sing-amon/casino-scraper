import scrapy


class Bet7kSpider(scrapy.Spider):
    name = "bet7k"
    allowed_domains = ["7k.bet.br"]
    start_urls = ["https://7k.bet.br/"]

    def parse(self, response):
        pass
