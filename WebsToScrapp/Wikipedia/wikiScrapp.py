import requests
from lxml import html

url = 'https://www.wikipedia.org/'
headers = { 'User-Agent': 'Mozilla/5.0' }
response = requests.get(url, headers=headers)

parser = html.fromstring(response.text)

wikis = parser.xpath("//div[@class='other-project-text']/span[@class='other-project-title jsl10n']")

if __name__ == '__main__':
    for wiki in wikis:
        print(wiki.text_content())