import urllib.request
import urllib.error
from lxml import etree

from . import url_manger


HEADERS = {
	# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	# 'Accept-Encoding': 'gzip, deflate, sdch',
	# 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
	# 'Cache-Control': 'max-age=0',
	# 'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}


class MySpider(object):
	"""
	Spider--Request,parse
	"""

	__REQUEST_HEADERS = HEADERS

	domain = ''
	start_url = ['', ]

	def __init__(self):
		self.url_mgr = url_manger.UrlManger()

		if self.domain.endswith('/'):
			self.domain = self.domain.rstrip('/')

	def Request(self, url_list, callback=None):
		"""
		get urls, return parse() or callback()
		"""
		request_list = map(lambda url: urllib.request.Request(url, headers=self.__REQUEST_HEADERS), url_list)
		response_list = self.Response(request_list)

		if callback is not None:
			return self.__get_items(response_list, callback)
		else:
			return self.__get_items(response_list, self.parse)

	def Response(self, request_list):
		def get_response(request):
			try:
				with urllib.request.urlopen(request) as resp:
					response = resp.read()
					return response
			except urllib.error.URLError:
				return None
		return map(get_response, request_list)

	def parse(self, response):
		response = response.xpath('*')
		return

	def __get_items(self, response_list, func):
		selector_list = map(etree.HTML, response_list)
		return map(func, selector_list)

	def url_join(self, href):
		return ''.join([self.domain, href])

	def crawl(self):
		self.url_mgr.add_new_urls(self.start_url)
		while self.url_mgr.has_new_url:
			new_url = self.url_mgr.get_new_url()
			self.Request(new_url)

