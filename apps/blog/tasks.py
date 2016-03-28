from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab


logger = get_task_logger(__name__)


@periodic_task(
	run_every=(crontab()), 
	name='print_hi_task', 
	ignore_result=True
	)
def print_sth_task():
	logger.info('Print Something ')
	print('----------per minute------------------')