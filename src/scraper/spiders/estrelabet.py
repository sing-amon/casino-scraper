import scrapy
from datetime import datetime


class EstrelabetSpider(scrapy.Spider):
    name = "estrelabet"
    allowed_domains = ["www.estrelabet.bet.br"]
    start_urls = ["https://www.estrelabet.bet.br/pb/jogos"]

    def parse(self, response):
        
        game_titles = response.css('span.game-title::text').getall()[:10]
        print(game_titles)

        for game in game_titles:
            
            yield {
                'name': game,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'casino': self.name,
            }
