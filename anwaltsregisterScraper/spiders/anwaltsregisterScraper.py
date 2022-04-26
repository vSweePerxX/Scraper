import scrapy

from anwaltsregisterScraper.items import AnwaltsregisterscraperItem, BvaiItem


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


class BvaiScraper(scrapy.Spider):
    name = 'bvaiCrawler'
    start_urls = ['https://www.bvai.de/ueber-uns/bai-mitglieder']

    def parse(self, response):
        for link in response.css('a.btn.btn-default::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_personPage)

    def parse_personPage(self, response):
        item = BvaiItem()

        item['name'] = response.xpath('//h2/text()').extract_first()
        item['adressPart1'] = response.css('div.col-8::text')[0].get()
        item['adressPart2'] = response.css('div.col-8::text')[1].get()
        item['partner'] = response.xpath('//div[@class="col-8"]/text()')[2].extract().replace("\r\n", "")\
            .replace("  ", "").replace("und", " ").replace("  "," / ")
        item['phone'] = response.xpath('//div[@class="col-8"]/text()')[3].extract()\
            .replace("\r\n", "").replace("  ", "").replace("und ", " / ")
        item['mail'] = " / ".join(response.xpath('//div[@class="col-8"]/a/text()[contains(., "@")]').extract())
        item['website'] = response.xpath('//div[@class="col-8"]/a/text()[contains(., "www")]').extract_first()
        #item['ManagingDirector_BoardMember'] = response.xpath('//div[@class="col-8"]/text()')[11].extract().replace("\r\n ", "").strip()
        yield item