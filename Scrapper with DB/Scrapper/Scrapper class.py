import requests
from bs4 import BeautifulSoup as bs
import re
import openpyxl

URL = r'https://www.ebay.com/b/Sony/bn_21835731'

regex = r'(?<=>)(.*?)(?=<)'

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0)'
            ' Gecko/20100101 Firefox/102.0',
            'Accept-Language': 'en-US'})


class Requests:

    def __init__(self):
        pass

    @staticmethod
    def send_request(url):
        webpage = requests.get(url, headers=HEADERS)
        return webpage

    def get_bs_object(self, url):
        webpage = self.send_request(url)
        soup = bs(webpage.content, features='lxml')
        return soup

    def get_results_from_find_title(self, url):
        soup = self.get_bs_object(url)
        result = soup.findAll('h3', attrs={'class': "s-item__title"})
        return result


r = Requests()
array_which_contains_data_from_scrape = []

data = r.get_results_from_find_title(URL)
for string in data:
    match = re.findall(regex, str(string))

    if match:
        array_which_contains_data_from_scrape.append(match)

print(array_which_contains_data_from_scrape)

