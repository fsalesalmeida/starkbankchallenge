from apscheduler.schedulers.blocking import BlockingScheduler
from src.business import invoices
import datetime
import random


def run_task():
    sched = BlockingScheduler()
    stop_time = datetime.datetime.now() + datetime.timedelta(minutes=1)

    @sched.scheduled_job('interval', minutes=1)
    def timed_job():
        if datetime.datetime.now() > stop_time:
            sched.remove_all_jobs()
            sched.shutdown(wait=False)
        else:
            invoices.create(random.randrange(8, 12))

    sched.add_job(timed_job)
    sched.start()
