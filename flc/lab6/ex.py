from bs4 import BeautifulSoup
import requests
import re

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 1. 
header=soup.find("div", attrs={"class":"col-sm-8 h1"})
print(header.text)
page = soup.find("li", class_="current")
print("Current Page:", page.text.strip())

# 2. 
buttons = soup.find_all("button")
for button in buttons:
    print("Button Content:", button.text)

# 3.
products = soup.find_all(class_="product_pod")
for product in products:
    
    title = product.h3.a["title"]
    print("Product Title:", title)
    
    
    price = product.find(class_="price_color").text
    print("Product Price:", price)

# 4.
categories = soup.find("ul", class_="nav nav-list").find_all("li")
for category in categories:
    category_name = category.text.strip()
    print("Category:", category_name)

# 5.
images = soup.find_all("img")
for img in images:
    alt_text = img.get("alt", "")
    print("Image Alt Text:", alt_text)
