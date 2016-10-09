from django.shortcuts import render
from newspaper import Article
import newspaper


def home(request):
    """
    Entry point into the app
    :param request that will be handle by the url
    :return: renders the home page
    """
    context = {'news': fetch_news()}
    return render(request=request, template_name='index.html')


def fetch_news():
    """
    fetch the news and blog posts for the blogs and news section
    :return: a dictionary with the blogs and news items
    """
    news = {}

    bloomberg = newspaper.build("http://www.bloomberg.com/europe")

    # get the urls and pass them into Article
    for news_articles in bloomberg.articles:
        count = 1
        article = Article(news_articles.url)
        article.download()
        article.parse()
        news["news" + str(count)] = {'authors': article.authors,
                                     "date": article.publish_date,
                                     'text': article.text,
                                     'top_image': article.top_image,
                                     "movies": article.movies,
                                     }
        count += 1
    return news