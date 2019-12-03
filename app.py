from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/news")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/news"
# mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    news=mongo.db.news.find_one()
    return render_template("index.html", news=news)

# Route that will trigger the scrape function

@app.route("/scrape")
def scrape():

   # Run the scrape function
    news=mongo.db.news
    news_data=scrape_mars.scrape()
    news.update({}, news_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

