import datetime
import time
import pytz
import random
from apps.spider.spider_module.spider import MySpider
from apps.spider.models import Calendar


class MafengwoSpider(MySpider):
	domain = 'http://www.mafengwo.cn'
	start_url = [
		'http://www.mafengwo.cn/app/calendar.php?year=2016', 
		'http://www.mafengwo.cn/app/calendar.php?year=2015', 
		'http://www.mafengwo.cn/app/calendar.php?year=2014', 
		'http://www.mafengwo.cn/app/calendar.php?year=2013',
	]

	def parse(self, response_and_url):
		response = response_and_url[0]
		urls = set()
		for href in response.xpath("//li[@class='_j_hover']/span[@class='mark']/a[1]/@href"):
			urls.add(self.url_join(href))
		return urls
		# return self.Request(url, callback=self.parse_dir_item)

	def parse_dir_item(self, response_and_url):
		response = response_and_url[0]
		
		try:
			item = {}
			item['url'] = response_and_url[1]
			item['title'] = response.xpath("//div[@id='_j_cover_box']/div[@class='_j_titlebg']/div[@class='view_info']/div[@class='vi_con']/h1/text()")[0].strip()
			item['img_src'] = response.xpath("//div[@id='_j_cover_box']/div[@class='set_bg _j_load_cover']/img/@src")[0]
			item['ding_num'] = int(response.xpath("//div[@class='ding']/a/@data-vote")[0])
			item['destinaion'] = response.xpath("//div[@class='mdd_info']/a/strong/text()")[0].strip()

			created_at = response.xpath("//div[@class='person']/div[@class='vc_time']/span[@class='time']/text()")[0].strip()
			created_at = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M').replace(tzinfo=pytz.timezone('Asia/Shanghai'))
			item['created_at'] = created_at

		except IndexError:
			return
		
		obj, created = Calendar.objects.update_or_create(url=item['url'], defaults=item)
		
		print('-------------------------------------')
		print(item['title'])

	def crawl(self):
		counter = 0
		
		self.url_mgr.add_new_urls(self.start_url)
		
		while self.url_mgr.has_new_url:
			counter += 1
			
			if counter == 10:
				time.sleep(random.randint(5, 15))
				counter = 0
			
			new_url = self.url_mgr.get_new_url()
			
			if new_url in self.start_url:
				new_url_list = list(self.Request([new_url, ]))[0]
				self.url_mgr.add_new_urls(new_url_list)
			else:
				list(self.Request([new_url, ], callback=self.parse_dir_item))