import requests
from bs4 import BeautifulSoup

def scrape_and_extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('h2').text
            content = article.find('div', class_='content').text
            print(f"Title: {title}\nContent: {content}\n")

url_to_scrape = 'https://newswebsite.com'
scrape_and_extract(url_to_scrape)
