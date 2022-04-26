# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnwaltsregisterscraperItem(scrapy.Item):
    # define the fields for your item here like:
    calledTitle = scrapy.Field()
    name = scrapy.Field()
    jobTitle = scrapy.Field()
    street_nr = scrapy.Field()
    postcode = scrapy.Field()
    addressLocality = scrapy.Field()
    state = scrapy.Field()
    tel = scrapy.Field()
    mobile = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()

class BvaiItem(scrapy.Item):

    name = scrapy.Field()
    adressPart1 = scrapy.Field()
    adressPart2 = scrapy.Field()
    partner = scrapy.Field()
    phone = scrapy.Field()
    mail = scrapy.Field()
    website = scrapy.Field()
    ManagingDirector_BoardMember = scrapy.Field()