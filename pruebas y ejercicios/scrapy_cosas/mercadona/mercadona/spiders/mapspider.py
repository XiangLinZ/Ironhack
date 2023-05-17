from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner
import extruct

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

class MapspiderSpider(CrawlSpider):
    name = 'mapspider'
    allowed_domains = ['tienda.mercadona.es']
    start_urls = ['http://tienda.mercadona.es/']
    rules = (Rule(LinkExtractor()),)


    def parse_item(self, response):
        yield {
            'url': response.url,
            'metadata': extruct.extract(
                response.text,
                response.url,
                syntaxes=['opengraph', 'json-ld']
            ),
        }