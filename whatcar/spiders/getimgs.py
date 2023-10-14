import scrapy
from os import getenv

class GetimgsSpider(scrapy.Spider):
    name = "getimgs"
    allowed_domains = ["www.carsales.com.au"]
    make_model=getenv("model")
    newmake_model_text = make_model.replace(" ", "%20")
    make, model = make_model.split('/')
    print(f"make ------------- {make}")
    print(f"model -------------{model}")
    start_urls = [f"https://www.carsales.com.au/cars/?q=(And.Service.carsales._.Year.range(2020..)._.(C.Make.{make}._.Model.{model}.))&offset=0"]
    
    page_count = 1
    def parse(self, response):
        if self.page_count > 9:
            return
        pass
    
        print("----------output -------------")
        img_urls = response.xpath("//div[@class='carousel-inner']/div[@class='carousel-item active image']/img/@src").getall()
        for img_url in img_urls:
            yield {
                "img_url":img_url
            } 
        
        next_page_relative=response.xpath("//a[@class='page-link next ']/@href").get()
        next_page_absolute=response.urljoin(next_page_relative)
        print(next_page_absolute)

        if next_page_absolute:
            self.page_count += 1
            yield scrapy.Request(url=next_page_absolute,callback=self.parse)
        
