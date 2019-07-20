import scrapy

class HudhomestoreSpider(scrapy.Spider):
    name = 'Hudhomestore'

    def start_requests(self):
        url = """https://www.hudhomestore.com/Listing/PropertySearchResult.aspx?pageId=1&sPageSize=1000&
        zipCode=&city=&county=&sState=TX&fromPrice=0&toPrice=0&fCaseNumber=&bed=0&bath=0&street=&buyerType=0&
        specialProgram=&Status=0&indoorAmenities=&outdoorAmenities=&housingType=&stories=&parking=&propertyAge=&
        OrderbyName=SCASENUMBER&OrderbyValue=ASC&sLanguage=ENGLISH"""
        
        yield scrapy.Request(url=url, callback=self.parse)

    """
        page = response.url.split("/")[-2]
        filename = 'HUD-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
    """
    def parse(self, response):
        filename = 'HUD.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)


        #propertylistings = response.xpath("//tr[contains(@class,'FormTableRow')]").getall()
        #print(len(propertylistings))
        
        #print(propertylistings[2].xpath("(//u/text())[1]").get())


        #for house in propertylistings:
        #    print(house.xpath("//u/text()").get())