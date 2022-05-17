import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By

from anwaltsregisterScraper.items import AnwaltsregisterscraperItem, BvaiItem, GelbeSeitenItem


class AnwaltsregisterScraper(scrapy.Spider):
    name = 'anwaltCrawler'

    def __init__(self, bundesland=''):
        global test
        test = bundesland
        self.start_urls = [f'https://www.anwaltsregister.de/Anwaelte_aus_Deutschland/Rechtsanwalt_in_{bundesland}.html']

    def parse(self, response):
        item = AnwaltsregisterscraperItem()
        # for results in response.xpath('//li[@layout]'):
        for link in response.xpath('//li[@layout]').css('a ::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_personPage)

        next_page_part = response.xpath('//div[@class="navLink nextLink"]/a/@href').extract_first()

        if next_page_part is not None:
            yield scrapy.Request(next_page_part, callback=self.parse)

    def parse_personPage(self, response):
        item = AnwaltsregisterscraperItem()

        item['Title'] = response.css('span.calledTitle::text').get()
        item['Name'] = response.xpath('//h1[@class="attorneyName"]/text()').get()
        item['Spezialisierung'] = response.css('span.jobTitle::text').get()
        item['Straße_Hausnummer'] = response.css('p.address1::text').get()
        item['PLZ'] = response.css('p.address2').xpath('//span[@itemprop="postalCode"]/text()').extract_first()
        item['Ort'] = response.css('p.address2').xpath(
            '//span[@itemprop="addressLocality"]/text()').extract_first()
        item['Bundesland'] = test
        item['Festnetz'] = response.xpath('//p[@class="callnumber1"]/span[@class="data"]/text()').get()
        item['Mobile'] = response.xpath('//p[@class="cellphone"]/span[@class="data"]/text()').get()
        item['Fax'] = response.xpath('//p[@class="telefax"]/span[@class="data"]/text()').get()
        item['Email'] = response.xpath('//p[@class="emailLink"]/a[@class="data"]/@href').extract_first()
        item['Website'] = response.xpath('//p[@class="homepageLink"]/a[@class="data"]/@href').extract_first()
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
        item['partner'] = response.xpath('//div[@class="col-8"]/text()')[2].extract().replace("\r\n", "") \
            .replace("  ", "").replace("und", " ").replace("  ", " / ")
        item['phone'] = response.xpath('//div[@class="col-8"]/text()')[3].extract() \
            .replace("\r\n", "").replace("  ", "").replace("und ", " / ")
        item['mail'] = " / ".join(response.xpath('//div[@class="col-8"]/a/text()[contains(., "@")]').extract())
        item['website'] = response.xpath('//div[@class="col-8"]/a/text()[contains(., "www")]').extract_first()
        # item['ManagingDirector_BoardMember'] = response.xpath('//div[@class="col-8"]/text()')[11].extract().replace("\r\n ", "").strip()
        yield item

        # response.xpath('//h2[@data-wipe-name="Titel"]/text()').extract_first()


class GelbeSeitenScraper(scrapy.Spider):
    name = 'gelbeSeitenCrawler'
    start_urls = ['https://www.gelbeseiten.de/Suche/Immobilienverwaltung/Bundesweit']

    def parse(self, response):
        driver = webdriver.Chrome(
            '/Users/janbenno/Desktop/IntelaJ/DataCollecter/anwaltsregisterScraper/webDriver/chromedriver')

        driver.get(
            'https://www.gelbeseiten.de/Suche/Immobilien/Bundesweit')
        button = driver.find_element(By.XPATH, "//div[@class='cmpboxbtns']/span[@id='cmpwelcomebtnyes']/a")
        button.click()
        counter = 0
        while driver.find_element(By.XPATH, "//form[@id='mod-LoadMore']/a[@id='mod-LoadMore--button']") is not None:
            try:
                button = driver.find_element(By.XPATH, "//form[@id='mod-LoadMore']/a[@id='mod-LoadMore--button']")
                button.click()
                ++counter
            except:
                break
                print('Counter', counter)


# self.driver.close()

def parse_personPage(self, response):
    item = GelbeSeitenItem()

    item['name'] = response.css('h1::text').get()
    item['straße_Hausnummer'] = \
        response.xpath('.//address[@class="mod-TeilnehmerKopf__adresse :: d-none d-md-block"]/span/text()')[0].extract()
    item['PLZ'] = response.xpath('.//address[@class="mod-TeilnehmerKopf__adresse :: d-none d-md-block"]/span/text()')[
        1].extract()
    item['Branche'] = response.xpath('.//div[@class="mod-TeilnehmerKopf__branchen"]/span/text()').extract_first()
    yield item
