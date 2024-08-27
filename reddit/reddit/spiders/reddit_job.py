# -*- coding: utf-8 -*-
import scrapy

from reddit.items import RedditItem
from scrapy.http.request import Request


class RedditJobSpider(scrapy.Spider):

    name = 'reddit_job'

    # where to extract data
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/funny/']


    def parse(self, response):

    	# how to extract data
        titles = response.css("a.title::text").extract()
        hrefs = response.css("a.title::attr(href)").extract()
        scores = response.css("div.score.unvoted::attr(title)").extract()

        for item in zip(titles, hrefs, scores):

        	new_item = RedditItem()

        	new_item['title'] = item[0]
        	new_item['href'] = item[1]
        	new_item['score'] = item[2]

        	yield new_item

        next_page = response.css('span.next-button').css('a::attr(href)').extract()[0]

        yield Request(url=next_page, callback=self.parse)