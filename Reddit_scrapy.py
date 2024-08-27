from typing import Any
import scrapy
from scrapy.http import Response

class RedditJobSpider(scrapy.Spider):
    
    name = 'reddit_job'
    
    
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/t/animals_and_pets/']
    
    
    def parse(self, response):
        #return super().parse(response, **kwargs)
    
        print (response.css("a.title::text").extract())
        print (response.css("a.title::attr(href)").extract())
        print (response.css("div.score.unnoted::attr(title)").extract())
        
    