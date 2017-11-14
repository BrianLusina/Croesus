"""
View functions that will be responsible for creating JSON response for fetched blog and 
news posts

This will be used for displaying relevant data to client side code.
No template is rendered, neither are static files loaded. This will be used to display
data from various news articles and sites. client will handle static files and HTML page 
rendering.
"""
from flask import jsonify
import redis
import json
import os
from app.mod_blog.tasks import fetch_news
from . import blog

r = redis.StrictRedis(host='localhost',
                      port=os.environ.get("REDIS_PORT", 6379),
                      db=os.environ.get("REDIS_DB", 0))


@blog.route("", methods=["GET", "POST"])
@blog.route("/", methods=["GET", "POST"])
def display_top_news():
    """
    Will create a proper JSON response for the top news to display to the client
    Accessed via route <API_URL>/blog/
    :return: JSON response of data related to blog posts and news
    """
    for key in r.keys():
        value = r.get(key.decode("utf-8"))
        if value:
            val_ = value.decode("utf-8")
            results = val_.split(",")
            print("Res", results)

    return jsonify({
        "message": "Could not fetch blog posts at the moment",
    }), 200
