import requests
from bs4 import BeautifulSoup
import psycopg2
import json

url = """http://books.toscrape.com"""

response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

#title = soup.find().get_text.strip()

title = soup.find("title").text

categories = soup.find(class_ = "nav nav-list")

listed = categories.find_all("li")


book_dictionary = {}


#The code below obtained the books in all categories and saved them in the dictionary
for item in listed:

    listed = item.find("a")

 
    if listed is not None:
        listed_category = listed.text.strip()
        listed_link = listed.get("href")

        book_page = requests.get("http://books.toscrape.com/"+listed_link)

        book_html_content = book_page.text
        book_soup = BeautifulSoup(book_html_content, 'html.parser')

        travel_title = book_soup.find("title").text
        product_list = book_soup.find_all(class_ = "product_pod")
        
        item_property = {}

        for book_item in product_list:
            book_title = book_item.find("h3").text
            book_price = book_item.find(class_ = "price_color").text[1:]
            
            item_property["Title"] = book_title
            item_property["Price"] = book_price

        
        book_dictionary[listed_category] = item_property


# print(book_dictionary)

#storing the dictionary data in a postgre database

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Bookscrape",
    user="postgres",
    password="#Tolexy5038"
)

json_data = json.dumps(book_dictionary)



#the code below created a table in the database
# cur = conn.cursor()

# create_table_query = """
# CREATE TABLE Bookinfo (
#     Category VARCHAR(50) PRIMARY KEY,
#     Bookname VARCHAR(50),
#     Bookprice VARCHAR(50)
# )
# """
# cur.execute(create_table_query)
# cur.close()

#the code below insert the dic in the table
cur = conn.cursor()

create_table_query = """
CREATE TABLE Bookinfos (
    cardata JSONB
)
"""

cur.execute(create_table_query)

cur.execute("INSERT INTO Bookinfos (cardata) VALUES (%s)", (json_data,))
conn.commit()
cur.close()