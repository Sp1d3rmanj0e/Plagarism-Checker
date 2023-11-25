import requests
from bs4 import BeautifulSoup

def fetch_data(site_url):
    result = requests.get(site_url)
    if result.status_code == 200:
        bs_object = BeautifulSoup(result.content, 'html.parser')
        hyperlinks = bs_object.find_all('a')
        for link in hyperlinks:
            print(link.get('href'))

target_url = 'https://example.com'
fetch_data(target_url)
