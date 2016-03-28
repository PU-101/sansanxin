import scrapy
from spider.items import SpiderItem

class MafengwoSpider(scrapy.Spider):
	name = 'mafengwo'
	allowed_domains = ['http://www.mafengwo.cn/']
	start_urls = [
		'http://www.mafengwo.cn/app/calendar.php?year=2016',
	]

	def parse(self, response):
		for href in response.xpath("/html/body/div[@class='wrapper']/div[@class='calendar']/div[@class='bd']/div[@class='viewport']/div/ul//li[@class='_j_hover']/span[@class='mark']/a[1]/@href"):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse(self, response):
		item = SpiderItem()
		item['title'] = response.xpath("//*[@id='_j_cover_box']/div[5]/div[2]/div/h1\text()").extract()
		
		yield item