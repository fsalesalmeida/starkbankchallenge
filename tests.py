import names
import random
from src.utils import random_cpf

# from apscheduler.schedulers.blocking import BlockingScheduler
# import datetime
# import time
#
# sched = BlockingScheduler()
# stop_time = datetime.datetime.now() + datetime.timedelta(seconds=30)
#
#
# @sched.scheduled_job('interval', seconds=5)
# def timed_job():
#     if datetime.datetime.now() > stop_time:
#         sched.remove_all_jobs()
#         sched.shutdown(wait=False)
#     else:
#         invoice_quantity = random.randrange(8, 12)
#         print(f'Numero de Faturas: {invoice_quantity}')
#
#
# sched.add_job(timed_job)
# sched.start()


# create_invoices()
#
# invoice_quantity = random.randrange(8, 12)

cpf = random_cpf.generate()
print(cpf)
print(type(cpf))

print(random.randint(10000, 99999))

print(names.get_full_name())
