import scrapy

class LandcrawlSpider(scrapy.Spider):
    name = 'landcrawl'
    start_urls = [
        'https://www.rumah.com/properti-dijual?listing_type=sale&market=residential&property_type=L&property_type_code[]=RLAND&district_code=IDJI29&freetext=Surabaya&search=true',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'links': quote.css('a').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)