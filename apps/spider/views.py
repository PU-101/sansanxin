from django.shortcuts import render
from apps.spider.mafengwo import MafengwoSpider
from django.http import HttpResponse

# Create your views here.
# def index(request):
# 	spider = MafengwoSpider()
# 	spider.crawl()
# 	return HttpResponse('finished')