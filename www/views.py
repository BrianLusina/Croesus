from django.shortcuts import render
from newspaper import Article


def home(request):
    """
    Entry point into the app
    :param request that will be handle by the url
    :return: renders the home page
    """
    return render(request=request, template_name='index.html')


def fetch_news():
    """
    fetch the news and blog posts for the blogs and news section
    :return: a dictionary with the blogs and news items
    """
    pass