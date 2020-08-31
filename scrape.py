#web scraping hacker news using beautifulsoup4 library
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.find_all('span'))

links = soup.select('.storylink')
votes = soup.select('.score')

print(links[0], votes[0])




