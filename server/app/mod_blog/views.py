"""
View functions that will be responsible for creating JSON response for fetched blog and 
news posts

This will be used for displaying relevant data to client side code.
No template is rendered, neither are static files loaded. This will be used to display
data from various news articles and sites. client will handle static files and HTML page 
rendering.
"""
from . import blog
from flask import jsonify, request, url_for
from app import celery
import newspaper


@blog.route("")
def display_top_news():
    """
    Will create a proper JSON response for the top news to display to the client
    :return: JSON response of data related to blog posts and news
    """

    fetch_news.delay()


@celery.task
def fetch_news():
    """
    fetch the news and blog posts for the blogs and news section
    This will be done on a different thread
    :return: a dictionary with the blogs and news items
    """
    results = []
    investopedia = newspaper.build("http://www.investopedia.com/")

    for categories in investopedia.category_urls():
        results.append(categories)
    return results
