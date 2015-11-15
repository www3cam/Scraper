'''
Created on May 30, 2015

@author: www3cam
'''

import scrapy
import csv

class SecSpider(scrapy.Spider):
    name = "SEC"
    allowed_domains = ["sec.gov"]
    domains = [''] * 2973
    i = 0
    j = 0
    sectors = {'Investment Firms': []}
    with open('C:\Users\www3cam\Cameron Work\Quandl\Quandl.csv', 'r') as csvfile:
        reader1 = csv.reader(csvfile)
        for row1 in reader1:
            ticker = str(row1)[7:-2]
            domains[i] = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK=' + ticker + '&Find=Search&owner=exclude&action=getcompany'
            i = i + 1
        maxlen = i 
    start_urls = domains
    
    def parse(self, response):
        filename = response.url[44:-44]
        #Industrycode = response.xpath('//title/text()')
        #Industrycode = response.xpath('//a[contains(@href, "/cgi-bin/browse-edgar?action=getcompany&amp;SIC"]/@href').extract()
        Industrycode = response.xpath('//p/a[1]/text()').extract()
        Industrycode2 = str(Industrycode)[3:-2]
        if self.sectors.has_key(Industrycode2):
            arrayindustry = self.sectors.get(Industrycode2,"error")
            arrayindustry.append(filename)
            self.sectors[Industrycode2] = arrayindustry
        elif self.is_number(Industrycode2) or Industrycode2 == '':
            array = [filename]
            self.sectors[Industrycode2] = array
        else:
            arrayindustry = self.sectors.get('Investment Firms',"error")
            arrayindustry.append(filename)
            self.sectors['Investment Firms'] = arrayindustry
        self.j = self.j + 1
        if self.j == self.maxlen: #should be the max number
            with open('C:\Users\www3cam\Cameron Work\Quandl\Quandledited.csv', 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
                for key in self.sectors.keys():
                    arraysector = [key]
                    arraysector.extend(self.sectors[key])
                    spamwriter.writerow(arraysector)
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
