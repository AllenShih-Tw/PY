import requests
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
r = requests.get('https://tw.yahoo.com/')

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 以 CSS 的 class 抓出各類頭條新聞
  stories = soup.find_all('a', class_='story-title')
  for a in stories:
    # 新聞標題
    print("標題：" + a.text)
    # 新聞網址
    print("網址：" + a.get('href'))