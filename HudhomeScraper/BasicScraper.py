# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:51:11 2019

@author: David


"""
import requests, pandas as pd
from bs4 import BeautifulSoup

class HudhouseListing:
    df = pd.DataFrame()
    results =[]
    
    def __init__(self):
        
        url = """https://www.hudhomestore.com/Listing/PropertySearchResult.aspx?pageId=1&sPageSize=1000&
        zipCode=&city=&county=&sState=TX&fromPrice=0&toPrice=0&fCaseNumber=&bed=0&bath=0&street=&buyerType=0&
        specialProgram=&Status=0&indoorAmenities=&outdoorAmenities=&housingType=&stories=&parking=&propertyAge=&
        OrderbyName=SCASENUMBER&OrderbyValue=ASC&sLanguage=ENGLISH"""

        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")    
        self.results = soup.find_all('tr',class_=['FormTableRow','FormTableRowAlt'])
        self.processCaseNumber()
        self.processAddress()
        self.processPrice()
        self.processStatus()
        print(type(self.results))
        
    def processCaseNumber(self):
        CaseNumber = []
        for x in self.results:
            CaseNumber.append(x.find('u').text)
        self.df['CaseNumber']=CaseNumber

    def processAddress(self):
        Address = []
        for x in self.results:
            for y in x.findAll('br'):
                y.replace_with(' ')
            Address.append(x.find('span').text.strip())
        self.df['Address']=Address
    
    def processPrice(self):
        Price = []
        for x in self.results:
            Price.append(x.find('b').text)
        self.df['Price']=Price
        
    def processStatus(self):
        Status = []
        for x in self.results:
            temp = x.find_all('label')[2].find('img')
            if(temp):
                Status.append(temp['title'])
            else:
                Status.append("No Change")
        self.df['Status']=Status
    
    
blah = HudhouseListing()

print(blah.df[blah.df['Status'] != "No Change" ])