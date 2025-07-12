from functools import wraps
from typing import Callable
from apscheduler.triggers.cron import CronTrigger

# Store registered cron jobs
cron_jobs = []


def cron(trigger: CronTrigger):
    """
    Decorator for registering cron jobs similar to FastAPI endpoints

    Usage:
        @cron(CronTrigger(day_of_week="sun", hour=17, minute=0))
        async def my_weekly_job():
            # job logic here
    """

    def decorator(func: Callable) -> Callable:
        # Store the job for later registration
        cron_jobs.append((func, trigger))

        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        return wrapper

    return decorator
