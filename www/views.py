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
    print(context)
    return render(request=request, template_name='index.html')


def fetch_news():
    """
    fetch the news and blog posts for the blogs and news section
    :return: a dictionary with the blogs and news items
    """
    news = {}

    motley_fool_investingnews = newspaper.build("http://www.fool.com/investing-news/")
    african_market_news = newspaper.build("https://www.african-markets.com/en/news")

    # get the urls and pass them into Article
    for news_articles in motley_fool_investingnews.articles:
        count = 0
        article = Article(news_articles.url)
        article.download()
        article.parse()
        article.nlp()
        news = {"news" + str(count): {'authors': article.authors,
                                      "date": article.publish_date,
                                      'text': article.text,
                                      'top_image': article.top_image,
                                      "movies": article.movies,
                                      "summary": article.summary
                                      }
                }
        count += 1

    return news
