from typing import Any
import scrapy
from scrapy.http import Response

class RedditJobSpider(scrapy.Spider):
    
    name = 'reddit_job'
    
    
    allowed_domains = ['reddit.com']
    start_urls = ['http://wwww.reddit.com/r/funny/']
    
    
    def parse(self, response):
        #return super().parse(response, **kwargs)
    
        print (response.css("a.title::text").extract())
        print (response.css("a.title::attr(href)").extract())
        print (response.css("div.score.unvoted::attr(title)").extract())
        
    