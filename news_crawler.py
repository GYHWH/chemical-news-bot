import requests
from bs4 import BeautifulSoup

class NewsCrawler:
    def __init__(self, url):
        self.url = url

    def fetch_news(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return self.parse_news(response.content)
        else:
            print(f'Failed to fetch news, status code: {response.status_code}')
            return []

    def parse_news(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        headlines = []
        for item in soup.find_all('h2'):  # Modify as per the website structure
            headlines.append(item.get_text())
        return headlines

if __name__ == '__main__':
    url = 'https://example.com/news'  # Replace with the actual news URL
    crawler = NewsCrawler(url)
    news = crawler.fetch_news()
    for headline in news:
        print(headline)