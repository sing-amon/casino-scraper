import scrapy


class KtoSpider(scrapy.Spider):
    name = "kto"
    allowed_domains = ["www.kto.bet.br"]
    start_urls = ["https://www.kto.bet.br/cassino/"]

    def parse(self, response):
        pass
