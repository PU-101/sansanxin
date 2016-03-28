import urllib.request 
import urllib.parse

HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Host': 'www.mafengwo.cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}


class MySpider(object):
	REQUEST_HEADERS = HEADERS

	domain = ''
	start_url = ''

	# def encodeData(self, post_data):
	# 	return urllib.parse.urlencode(post_data)

	def Request(self, url, query=None, callback=None):
		return urllib.request.Request(self.start_url, query, REQUEST_HEADERS)

	def get_response(self, request):
		return urllib.request.urlopen(request)

	def parse(self):
		pass




