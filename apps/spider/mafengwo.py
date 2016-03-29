import datetime
from apps.spider.spider_module.spider import MySpider
from apps.spider.models import MafengwoModel


class MafengwoSpider(MySpider):
	domain = 'http://www.mafengwo.cn'
	start_url = ['http://www.mafengwo.cn/app/calendar.php?year=2016', ]

	def parse(self, response_and_url):
		response = response_and_url[0]
		urls = set()
		for href in response.xpath("//li[@class='_j_hover']/span[@class='mark']/a[1]/@href"):
			urls.add(self.url_join(href))
		return urls
		# return self.Request(url, callback=self.parse_dir_item)

	def parse_dir_item(self, response_and_url):
		response = response_and_url[0]
		item = {}
		item['url'] = response_and_url[1]
		title = response.xpath("//div[@id='_j_cover_box']/div[@class='_j_titlebg']/div[@class='view_info']/div[@class='vi_con']/h1/text()")
		if not title:
			return
		else:
			item['title'] = title[0].strip()
		item['image_src'] = response.xpath("//div[@id='_j_cover_box']/div[@class='set_bg _j_load_cover']/img/@src")[0].strip()
		created_at = response.xpath("//div[@class='person']/div[@class='vc_time']/span[@class='time']/text()")[0].strip()
		created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')
		item['created_at'] = created_at
		obj, created = MafengwoModel.objects.update_or_create(url=item['url'], defaults=item)
		print('-------------------------------------')
		print(item['title'])

	def crawl(self):
		self.url_mgr.add_new_urls(self.start_url)
		while self.url_mgr.has_new_url:
			new_url = self.url_mgr.get_new_url()
			if new_url == self.start_url:
				new_url_list = list(self.Request(new_url))[0]
				self.url_mgr.add_new_urls(new_url_list)
			else:
				list(self.Request(new_url, callback=self.parse_dir_item))