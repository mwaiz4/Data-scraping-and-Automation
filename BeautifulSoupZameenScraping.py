from bs4 import BeautifulSoup
import requests

url = "https://www.zameen.com/society_maps/"
req=requests.get(url)

#scrape
soup = BeautifulSoup(req.content, 'lxml')
card = soup.find('ul', class_="can-scroll")
cities = card.find_all("li", class_="searchbar_listItem__Gvwdu")

for item in cities:
    print(item.text)

with open("cities.txt", "w") as file:
    for item in cities:
        file.write(str(item.text) +"\n")





