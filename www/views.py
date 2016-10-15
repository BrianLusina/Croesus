from django.shortcuts import render
from newspaper import Article
import newspaper
from .forms import ContactForm


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
    investopedia = newspaper.build("http://www.investopedia.com/")

    for categories in investopedia.category_urls():
        print(categories)


def contact(request):
    """
    Handles the contact form, picks data and sends the contact form to server
    :param request: the request handle by this function
    :return:
    """
    if request.method == "POST":
        form = ContactForm(request.POST)


    pass