# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapytutItem


class ScrapyTutSpider(scrapy.Spider):
    name = "scrapytut"
    page_number = 2
    start_urls = [
        'http://localservices.sulekha.com/restaurants-in-bay-area'
    ]

    def parse(self, response):
        items = ScrapytutItem()
# BY USING CSS SELECTORS IT SELECT THE PARTICULAR ITEMS IN THE HTML PAGE USING THE CSS SELECTOR TAGS:
        containers = response.xpath("//div[@id='divaddviewmore']/div[@class='media']")
        for container in containers:
            crawlingpage_name = container.css(".media-heading span::text").extract()
            crawlingpage_address = container.css(".city-blk::text").extract()
            crawlingpage = container.css('.star-blk b::text').extract()
            if crawlingpage:
                crawlingpage_ratings = crawlingpage
            else:
                crawlingpage_ratings = "none"
            crawlingpage_reviews = container.css(".star-blk a::text").extract()
# AND SAVE ALL THE CRAWLED OUTPUT IN THE ITEMS
            items["crawlingpage_name"] = crawlingpage_name
            items["crawlingpage_address"] = crawlingpage_address
            items["crawlingpage_ratings"] = crawlingpage_ratings
            items["crawlingpage_reviews"] = crawlingpage_reviews
# THEN PRINT THE ITEMS
            yield items
# IF THE FIRST PAGE IS SCRALED THEN IT MOVE ON TO THE NEXT PAGE UNTILL THIS IF CONDITION SATISFIES:
        next_page = "http://localservices.sulekha.com/restaurants-in-bay-area_" + str(ScrapyTutSpider.page_number) + ""
        if ScrapyTutSpider.page_number <= 14:
            ScrapyTutSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
