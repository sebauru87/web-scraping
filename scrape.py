# web scraping hacker news using beautifulsoup4 library
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('span'))

links = soup.select('.storylink')
subtext = soup.select('.subtext')


# print(links[0], votes[0])

def create_my_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hacker_news.append({'title': title, 'link': href, 'votes': points})

    return hacker_news


# print(votes[0].getText())


print(create_my_news(links, subtext))
