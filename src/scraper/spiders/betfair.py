import scrapy


class BetfairSpider(scrapy.Spider):
    name = "betfair"
    allowed_domains = ["casino.betfair.bet.br"]
    start_urls = ["https://casino.betfair.bet.br/"]

    def parse(self, response):
        pass
