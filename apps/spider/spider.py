import urllib.request 
import urllib.parse

from lxml import etree

HEADERS = {
	# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	# 'Accept-Encoding': 'gzip, deflate, sdch',
	# 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
	# 'Cache-Control': 'max-age=0',
	# 'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}


class MySpider(object):
	__REQUEST_HEADERS = HEADERS

	domain = ''
	start_url = ['', ]

	@classmethod
	def __init__(cls):
		if cls.domain.endswith('/'):
			cls.domain = cls.domain.rstrip('/')

	def Request(self, url_list, callback=None):
		request_list = map(lambda url: urllib.request.Request(url, headers=self.__REQUEST_HEADERS), url_list)

		def get_response(request):
			with urllib.request.urlopen(request) as resp:
				response = resp.read()
				return response

		response_list = map(get_response, request_list)

		if callback is not None:
			return self.__get_items(response_list, callback)
		else:
			return self.__get_items(response_list, self.parse)

	def parse(self, response):
		response = response.xpath('*')
		return

	def __get_items(self, response_list, func):
		selector_list = map(etree.HTML, response_list)
		return list(map(func, selector_list))

	def url_join(self, href):
		return ''.join([self.domain, href])

	def run_spider(self):
		print(self.Request(self.start_url))


class BaiduSpider(MySpider):
	domain = 'http://www.mafengwo.cn'
	start_url = ['http://www.mafengwo.cn/app/calendar.php?year=2016', ]

	def parse(self, response):
		url = []
		for href in response.xpath("/html/body/div[@class='wrapper']/div[@class='calendar']/div[@class='bd']/div[@class='viewport']/div/ul//li[@class='_j_hover']/span[@class='mark']/a[1]/@href"):
			url.append(self.url_join(href))
		return self.Request(url, callback=self.parse_dir_item)

	def parse_dir_item(self, response):

		print(response.xpath("//li[@id='_j_cover_box']/div[5]/div[2]/div/h1/text()"))


	# def parse(self, response):
	# 	item = SpiderItem()
	# 	item['title'] = response.xpath("//*[@id='_j_cover_box']/div[5]/div[2]/div/h1\text()").extract()
		
	# 	yield item

b = BaiduSpider()
b.run_spider()





