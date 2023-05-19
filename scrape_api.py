import requests
from bs4 import BeautifulSoup
import psycopg2
import json
from flask import Flask, jsonify


app = Flask(__name__)

# PostgreSQL connection details
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Bookscrape",
    user="postgres",
    password="#Tolexy5038"
)


@app.route('/api/books', methods = ['GET'])
def get_cars ():

    cur = conn.cursor()

    fetch_table = "SELECT cardata FROM bookinfos"

    cur.execute(fetch_table)
    # Fetch all rows as a list of tuples
    rows = cur.fetchall()

    cur.close()


    cars = []

    for row in rows:
        car_data = row[0]
        car_data = str(car_data)
     
 
        cars.append(car_data)

    # Return the cars as JSON
    return jsonify(cars)

if __name__ == '__main__':
    app.run()
    