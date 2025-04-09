import scrapy


class SportingbetSpider(scrapy.Spider):
    name = "sportingbet"
    allowed_domains = ["casino.sportingbet.bet.br"]
    start_urls = ["https://casino.sportingbet.bet.br/pt-br/games"]

    def parse(self, response):
        pass
