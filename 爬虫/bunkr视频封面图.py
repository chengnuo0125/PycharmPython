"""
爬取 bunkr yuyuanyaya 上的视频封面图
2024.8.29
"""

import requests
from bs4 import BeautifulSoup
import time

url = "https://bunkr.si/a/gfcEpypB"  # 目标网址
head = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0"
}

response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")

all_divs = soup.find('section', attrs={'class': 'mx-auto py-5 px-4 sm:py-10 sm:px-6 lg:max-w-7xl lg:px-8'}).find_all(
    'div', attrs={
        'class': 'grid-images_box rounded-lg dark:bg-gray-200 xl:aspect-w-7 xl:aspect-h-8 p-2.5 border-2 display relative flex text-center'})
img_name = 1  # 图片名字

for each in all_divs:
    src = each.find('a').find('img').get('src')  # 图片链接
    img_response = requests.get(src, headers=head)
    img_content = img_response.content
    # 下载图片
    with open(f"img/{img_name}.png", 'wb') as f:
        f.write(img_content)
        print("over!!!", img_name)
        time.sleep(1)  # 等待 1 秒
    img_name += 1
print("all over!!!")
