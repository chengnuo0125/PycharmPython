"""
爬取 https://books.toscrape.com/ 上书的名字和价格
2024.8.29
"""


import requests
from bs4 import BeautifulSoup


head = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0"
}
content = requests.get('https://books.toscrape.com/', headers=head).text
soup = BeautifulSoup(content, 'html.parser')

# 价格
# all_prices = soup.find_all("p", attrs={"class": "price_color"})
# for each in all_prices:
#     print(each.string[2:])

# 书名
all_titles = soup.find_all('h3')
for title in all_titles:
    link = title.find("a")
    print(link.string)
