import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from spider_ebay.items import SpiderEbayItem,EbayItems


class EbaySpider(RedisCrawlSpider):
    name = 'ebay'
    allowed_domains = ['www.ebay.com']
    # start_urls = ['https://www.ebay.com/v/allcategories']
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 1,  # 延时最低为2s
    #     'AUTOTHROTTLE_ENABLED': True,  # 启动[自动限速]
    #     'AUTOTHROTTLE_DEBUG': True,  # 开启[自动限速]的debug
    #     'AUTOTHROTTLE_MAX_DELAY': 10,  # 设置最大下载延时
    #     'DOWNLOAD_TIMEOUT': 10,
    #     'CONCURRENT_REQUESTS_PER_DOMAIN': 4 }
    redis_key = "ebay_spider"

    # 动态域范围获取
    # def __init__(self, *args, **kwargs):
    #      #Dynamically define the allowed domains list.
    #      domain = kwargs.pop('domain', '')
    #      self.allowed_domains = filter(None, domain.split(','))
    #      super(EbaySpider, self).__init__(*args, **kwargs)
    page_lx = LinkExtractor(allow=('https://www.ebay.com/sch/[^\s]*/\d+/i.html',
                                              'https://www.ebay.com/sch/[^\s]*/\d+/i.html?_ipg=\d+&_pgn=\d+',
                                              'https://www.ebay.com/sch/[^\s]*/\d+/i.html?_pgn=\d+&_ipg=\d+'))
    rules = (
         Rule(page_lx, callback='parse_item', follow=True), )
  
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url,callback=self.parse)

    def parse_item(self, response):
        # print(response.url)
        divs = response.xpath("//div[@class='all-categories__cards']/div[@class='category-section']/div[@class='right-section side-cntr']/div//ul/li/a")

        for div in divs:
            item = SpiderEbayItem()
            item['link'] = div.xpath("./@href").extract()[0]
            item['title'] = div.xpath("./text()").extract()[0]
            # print(link,title)
            yield scrapy.Request(item['link'],callback=self.parse_detail)

    def parse_detail(self,response):
        li_list = response.xpath("//li[contains(@id,'w8-items')]")
        print(response.url)
        for li in li_list:
            # print(li)
            item = EbayItems()
            item['link'] = li.xpath(".//div[@class='s-item__info clearfix']/a/@href").extract_first()
            item['title'] = li.xpath(".//div[@class='s-item__info clearfix']/a/h3/text()").extract_first()
            item['price'] = ''.join(li.xpath(".//div[@class='s-item__info clearfix']/div//span[@class='s-item__price']/span/text()").extract())
            item['desc'] = li.xpath(".//div[@class='s-item__info clearfix']/div[@class='s-item__summary']/text()").extract()
            item['type'] = li.xpath(".//div[@class='s-item__info clearfix']/div[@class='s-item__details clearfix']/span[@class='s-item__detail s-item__detail--secondary']/span/text()").extract()
            item['is_shipping'] = li.xpath(".//div[@class='s-item__details clearfix']//span[@class='s-item__shipping s-item__logisticsCost']/text()").extract()
            # print('link:',link,'title:',title,'price:',price,'desc:',desc,'type:',type,'is:',is_shipping,sep='\n')
            print(item)
            yield item

        next_link = response.xpath("//*[@id='w5-w1']/a[2]/@href").extract_first()
        if next_link:
            yield scrapy.Request(next_link,callback=self.parse_item)
