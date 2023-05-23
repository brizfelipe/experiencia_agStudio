from datetime import timedelta

from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from action import main as action_main

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}


class ActionScheduler():

    def __init__(self):
        self.bk_sched_action = BackgroundScheduler(executors=executors)

    def activate(self):
        self.bk_sched_action.start()

    def addJob(self, functionName, argument):
        realFunction = getattr(action_main, functionName)
        self.bk_sched_action.add_job(lambda: realFunction(argument), 'date', run_date=timezone.now() + timedelta(seconds=1), name='run_action')
