from django.shortcuts import render
from apps.spider.mafengwo import MafengwoSpider
from django.http import HttpResponse

from .models import Calendar


# def index(request):
# 	spider = MafengwoSpider()
# 	spider.crawl()
# 	return HttpResponse('finished')


def get_destination_list(request):
    context_dict = {}
    cal_items = []
    if request.method == 'GET':
        mdd = request.GET['mdd']
        context_dict['mdd'] = mdd
        if mdd:
            cal_items = Calendar.objects.filter(destination=mdd)
            context_dict['cal_items'] = cal_items
        return render(request, 'destination/destination.html', context_dict)