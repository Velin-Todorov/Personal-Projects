import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import mysql.connector
import mysql


# DB - MySQL

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ozone_product_data'
)
mycursor = db.cursor()

# Building Excel Workbook
wb = Workbook()
worksheet = wb.active
worksheet.title = 'Product Info'
worksheet['A1'] = 'Product name'
worksheet['B1'] = 'Brand'
worksheet['C1'] = 'Price'
worksheet['D1'] = 'Availability'

# Building the Scrapper
HEADERS = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0)'
               ' Gecko/20100101 Firefox/102.0',
           'Accept-Language': 'en-US'}

product_links = []

for i in range(1, 4):
    ULR = f'https://www.ozone.bg/razopakovani/?limit=100&p={i}'
    webpage = requests.get(ULR, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'lxml')
    products = soup.find_all('div', class_='col-xs-3 five-on-a-row')

    for item in products:
        for link in item.find_all('a', href=True):
            product_links.append(link['href'])

count = 0

for product_link in product_links:
    count += 1
    webpage = requests.get(product_link, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'lxml')
    brand = ''

    try:
        name = soup.find('h1', attrs={'itemprop': 'name'}).text.strip()
    except:
        name = 'Not Available'

    try:
        attribute_list_to_obtain_brand = soup.find('ul', class_='attribute-list').text.strip().split()
    except:
        attribute_list_to_obtain_brand = []

    if attribute_list_to_obtain_brand:
        brand = attribute_list_to_obtain_brand[-1]

    try:
        price = soup.find('p', attrs={'class': 'special-price'}).text.strip().split('\n')[2].strip()
    except:
        price = 'Not Available'

    try:
        availability = soup.find('p', attrs={'id': 'availability-holder'}).text.strip().split('\t')[-1]
    except:
        availability = 'Not Available'

    # worksheet[f'A{count}'] = name
    # worksheet[f'B{count}'] = brand
    # worksheet[f'C{count}'] = price
    # worksheet[f'D{count}'] = availability


    mycursor.execute("INSERT INTO product_data VALUES(%s, %s,%s,%s,%s)", (count, name, brand, availability, price))
    db.commit()
    print(f'Product {count} data saved into database.')

# wb.save(r'C:\Users\velin\OneDrive\Desktop\Scrapper Project\Ozone Product Info.xlsx')
# print('Workbook saved. Scraping Completed!')
