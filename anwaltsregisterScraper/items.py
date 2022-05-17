# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnwaltsregisterscraperItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Name = scrapy.Field()
    Spezialisierung = scrapy.Field()
    Straße_Hausnummer = scrapy.Field()
    PLZ = scrapy.Field()
    Ort = scrapy.Field()
    Bundesland = scrapy.Field()
    Festnetz = scrapy.Field()
    Mobile = scrapy.Field()
    Fax = scrapy.Field()
    Email = scrapy.Field()
    Website = scrapy.Field()

class BvaiItem(scrapy.Item):

    name = scrapy.Field()
    adressPart1 = scrapy.Field()
    adressPart2 = scrapy.Field()
    partner = scrapy.Field()
    phone = scrapy.Field()
    mail = scrapy.Field()
    website = scrapy.Field()
    ManagingDirector_BoardMember = scrapy.Field()

class GelbeSeitenItem(scrapy.Item):

    name = scrapy.Field()
    #spezifikation = scrapy.Field()
    straße_Hausnummer = scrapy.Field()
    PLZ = scrapy.Field()
    Branche = scrapy.Field()