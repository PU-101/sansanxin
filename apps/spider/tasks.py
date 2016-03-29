from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab

from apps.spider.mafengwo import MafengwoSpider


logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab()), 
    name='crawl_mafengwo', 
    ignore_result=True
    )
def crawl_mafengwo_task():
    logger.info('Crawling...')
    spider = MafengwoSpider()
    spider.crawl()