"""
Tasks that will be carried out by celery when this module is called upon.

Will run tasks in the background and fetch related data
"""
from app import celery
# from app import redis_db
import json
import newspaper
import time


@celery.task(bind=True)
def fetch_news(self):
    """
    fetch the news and blog posts for the blogs and news section
    This will be done on a different thread
    :return: a dictionary with the blogs and news items
    """
    self.update_state(state="PENDING")

    results = []
    investopedia = newspaper.build("http://www.investopedia.com/")

    for categories in investopedia.category_urls():
        self.update_state(state="PROGRESS")
        results.append(categories)

    self.update_state(state="COMPLETE", meta={"result": results})
    time.sleep(1)

    return json.dumps(results)
