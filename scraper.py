import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
import requests
from bs4 import BeautifulSoup
import random

# app = Flask(__name__)

# @app.route('/')
def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")

    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue

        # Use this link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])
    return render_template("home.html")

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")

# if __name__ == "__main__":
    #runs the application on the repl development server
    # app.run(debug=True, port='8292', host='127.0.0.1')