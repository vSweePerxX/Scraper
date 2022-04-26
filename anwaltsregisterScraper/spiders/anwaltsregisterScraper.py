import scrapy

from anwaltsregisterScraper.items import AnwaltsregisterscraperItem


class AnwaltsregisterScraper(scrapy.Spider):
    name = 'anwaltCrawler'
    def __init__(self, bundesland=''):
        global test
        test = bundesland
        self.start_urls = [f'https://www.anwaltsregister.de/Anwaelte_aus_Deutschland/Rechtsanwalt_in_{bundesland}.html']

    def parse(self, response):
        item = AnwaltsregisterscraperItem()
        #for results in response.xpath('//li[@layout]'):
        for link in response.xpath('//li[@layout]').css('a ::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_personPage)


        #next_page_part = response.xpath('//div[@class="navLink nextLink"]/a/@href').extract_first()

        #if next_page_part is not None:
         #   yield scrapy.Request(next_page_part, callback=self.parse)



    def parse_personPage(self, response):
        item = AnwaltsregisterscraperItem()

        item['calledTitle'] = response.css('span.calledTitle::text').get()
        item['name'] = response.xpath('//h1[@class="attorneyName"]/text()').get()
        item['jobTitle'] = response.css('span.jobTitle::text').get()
        item['street_nr'] = response.css('p.address1::text').get()
        item['postcode'] = response.css('p.address2').xpath('//span[@itemprop="postalCode"]/text()').extract_first()
        item['addressLocality'] = response.css('p.address2').xpath('//span[@itemprop="addressLocality"]/text()').extract_first()
        item['state'] = test
        item['tel'] = response.xpath('//p[@class="callnumber1"]/span[@class="data"]/text()').get()
        item['mobile'] = response.xpath('//p[@class="cellphone"]/span[@class="data"]/text()').get()
        item['fax'] = response.xpath('//p[@class="telefax"]/span[@class="data"]/text()').get()
        item['email'] = response.xpath('//p[@class="emailLink"]/a[@class="data"]/@href').extract_first()
        item['website'] = response.xpath('//p[@class="homepageLink"]/a[@class="data"]/@href').extract_first()
        yield item


