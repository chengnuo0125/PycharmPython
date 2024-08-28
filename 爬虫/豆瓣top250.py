"""
爬取豆瓣电影 TOP250 的片名
2024.8.29
"""

import requests
from bs4 import BeautifulSoup

head = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0"
}

for start in range(0, 250, 5):  # 翻页功能
    content = requests.get(f'https://movie.douban.com/top250?start={start}&filter=', headers=head).text
    soup = BeautifulSoup(content, 'html.parser')
    all_titles = soup.find_all('span', attrs={"class": "title"})
    for each in all_titles:
        title = each.string
        if "/" not in title:
            print(title)
