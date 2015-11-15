# Scraper
Note: this code uses the external library Scrapy.  Consult their lisence before use.  


This describes the scraping program I wrote with Scrapy.  Basically I wrote a program to scrape the SEC website and find me industry classification codes for 3000 companies.  I was able to use these classification codes to come up with a list comps for all 3000 companies.  I was then able to use the commoditycorrel.m program in the Financial Programs section to test to see if companies that were comps could predict price movements of each other (a market cap weighted index was constructed in some cases, in others each individual stock was tested against other stocks that were comps).  
