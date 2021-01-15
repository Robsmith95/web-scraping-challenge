from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("./index.html", mars=mars)

# Scrape Route to Import `nasa_scraper.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars = mongo.db.mars
    mars_data = nasa_scraper.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()
#@app.route("/scrape")
#def echo():
   # return render_template("index.html", text="Serving up cool text from the Flask server!!")


#if __name__ == "__main__":
   # app.run(debug=True)