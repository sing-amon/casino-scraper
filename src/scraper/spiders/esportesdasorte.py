import scrapy


class EsportesdasorteSpider(scrapy.Spider):
    name = "esportesdasorte"
    allowed_domains = ["esportesdasorte.bet.br"]
    start_urls = ["https://esportesdasorte.bet.br/ptb/games/casino"]

    def parse(self, response):
        pass
