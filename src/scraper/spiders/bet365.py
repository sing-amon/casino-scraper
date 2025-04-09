import scrapy


class Bet365Spider(scrapy.Spider):
    name = "bet365"
    allowed_domains = ["casino.bet365.bet.br"]
    start_urls = ["https://casino.bet365.bet.br/home"]

    def parse(self, response):
        pass
