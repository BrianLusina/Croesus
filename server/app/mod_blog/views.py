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
# from app.mod_blog.blog_tasks import fetch_news


@blog.route("", methods=["GET", "POST"])
def display_top_news():
    """
    Will create a proper JSON response for the top news to display to the client
    Accessed via route <API_URL>/blog/
    :return: JSON response of data related to blog posts and news
    """
    try:
        # news_results = fetch_news.apply_async()

        # if news_results.state != "FAILURE":
        #     print(news_results)
        #     print("id", news_results.id)
        #     print("state", news_results.state)
        #     print("info", news_results.info)

            # return jsonify(news_results)
        return jsonify({}), 202
    except ValueError as ve:
        print(ve)


