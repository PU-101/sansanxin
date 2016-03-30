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
		response_and_url_list = self.Response(request_list, url_list)

		if callback is not None:
			return self.__get_items(response_and_url_list, callback)
		else:
			return self.__get_items(response_and_url_list, self.parse)

	def Response(self, request_list, url_list):
		def get_response(request):
			try:
				with urllib.request.urlopen(request) as resp:
					if resp.getcode() != 200:
						return None
					response = resp.read()
					return response
			except urllib.error.URLError:
				return None

		return zip(map(get_response, request_list), url_list)

	def parse(self, response_and_url):
		response = response_and_url[0].xpath('*')
		return

	def __get_items(self, response_and_url_list, func):
		# 删掉无效的元素
		selector_list = ((etree.HTML(response), url) for response, url in response_and_url_list if response is not None)		
		return map(func, selector_list)

	def url_join(self, href):
		return ''.join([self.domain, href])

	def crawl(self):
		self.url_mgr.add_new_urls(self.start_url)
		while self.url_mgr.has_new_url:
			new_url = self.url_mgr.get_new_url()
			self.Request(new_url)

