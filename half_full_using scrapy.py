import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class HalfFullSpider(CrawlSpider):
    name = 'half-full'
    allowed_domains = ['flashscore.com']
    start_urls = ['http://flashscore.com/']

    def parse(self, response):
        pass

        textInHeader = response.xpath('//html/body/div[5]/div/a/div').extract_first()

        texts = response.xpath('//html/body/div[5]/div/a/div').extract()

        yield {'textInHeader': textInHeader, 'texts': texts}