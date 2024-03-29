import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            yield {
                'name':book.css('h3 a::text').get(),
                'price':book.css('.product_price .price_color::text').get(),
                'url':response.css('h3 a').attrib['href'],
            }
        
        next_page =response.css('li.next a::attr(href)').get()  #Extracting URL of the next page
        
        if next_page is not None:   # Checking if there is a next page
            next_page_url = 'https://books.toscrape.com/' + next_page # Creating absolute URL for the next page
            yield response.follow(next_page_url, callback=self.parse)



#to select css  selector you can use the following code: 
'''
response.css('containerelement.class') to select all products
response.css('class selector a::text).get() - book.css('.product_price .price_color::text').get()
response.css(class selector a').attrib['href'](this will give you the link)
'''