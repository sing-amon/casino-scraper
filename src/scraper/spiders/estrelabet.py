import scrapy


class EstrelabetSpider(scrapy.Spider):
    name = "estrelabet"
    allowed_domains = ["www.estrelabet.bet.br"]
    start_urls = ["https://www.estrelabet.bet.br/pb/jogos"]

    def parse(self, response):
        pass
