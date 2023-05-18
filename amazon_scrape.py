import requests
from bs4 import BeautifulSoup

url = """http://books.toscrape.com"""

response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

#title = soup.find().get_text.strip()

title = soup.find("title").text

categories = soup.find(class_ = "nav nav-list")

listed = categories.find_all("li")


book_dictionary = {}

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


print(book_dictionary)





# book_url = "catalogue/category/books/travel_2/index.html"


# book_page = requests.get("http://books.toscrape.com/"+book_url)

# book_html_content = book_page.text
# book_soup = BeautifulSoup(book_html_content, 'html.parser')

# travel_title = book_soup.find("title").text
# product_list = book_soup.find_all(class_ = "product_pod")

# for book_item in product_list:
#     book_title = book_item.find("h3").text
#     book_price = book_item.find(class_ = "price_color").text[1:]
    

#     print(book_price)


