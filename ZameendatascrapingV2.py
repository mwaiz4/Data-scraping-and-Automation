#details in readme, 2nd data scraping project
from bs4 import BeautifulSoup
import requests
import time
global price
global card
global location
global currency
global bedrooms
global bathroom
global area
global data
def running():
    global card, price, location, currency, bedrooms, bathroom, area
    url = "https://www.zameen.com/Rentals_Flats_Apartments/Islamabad-3-1.html"
    req=requests.get(url)

    #scrape
    soup = BeautifulSoup(req.content, 'lxml')
    cards = soup.find_all('article')
    results = []
    for card in cards:
        price = card.find('div', {'class':'_2923a568'})
        location= card.find('div', {'aria-label':'Location'})
        bedrooms= card.find('span', { 'aria-label':'Beds'})
        bathroom= card.find('span', {'aria-label':'Baths'})
        area= card.find('span', {'aria-label':'Area'})

        results.append({
            'price': price.text.strip() if price else 'N/A',
            'location' : location.text.strip() if location else 'N/A',
            'bedrooms' : bedrooms.text.strip() if bedrooms else 'N/A',
            'bathroom' : bathroom.text.strip() if bathroom else 'N/A',
            'Area' : area.text.strip() if area else 'N/A'

        })
    return results
def write_to_file(data):
        global results
        with open('zameen_data.txt', 'w') as file:
            for item in data:
                file.write(f'''PRICE: {item['price']}
    LOCATION: {item['location']}
    BEDROOMS: {item['bedrooms']}
    BATHROOMS: {item['bathroom']}
    AREA: {item['Area']}

''')


while __name__=='__main__':
    data = running()
    write_to_file(data)
    time.sleep(10000)
