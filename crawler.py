# crawler.py
import scrapy

class WebCrawler(scrapy.Spider):
    name = "web_crawler"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(WebCrawler, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('url')]

    def parse(self, response):
        # Extract links and form elements
        links = response.css('a::attr(href)').getall()
        forms = response.css('form').getall()
        
        # Print the extracted data
        print("Links:", links)
        print("Forms:", forms)
        
        # Follow links to scrape further
        for link in links:
            if not link.startswith('http'):
                link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parse)

if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess()
    process.crawl(WebCrawler, url="https://juice-shop.herokuapp.com/")
    process.start()
