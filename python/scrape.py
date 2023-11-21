import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline a')
votes = soup.select('.score')

print(len(links))
print(len(votes))
#a = votes[1].select('.score')
#print(a[0].getText().replace(' points','').replace(' point',''))


def create_custom_hn(links, votes):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)

        vote = votes[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points','').replace(' point',''))
            print(points)
        
        hn.append({'title': title, 'link': href})
    return hn


create_custom_hn(links, votes)
