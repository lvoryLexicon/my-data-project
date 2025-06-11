import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

movies = []

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Referer": "https://movie.douban.com/",
    "Host": "movie.douban.com"
}

for start in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={start}"
    res = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.find_all("div", class_="item")
    print(f"✅ 正在抓取 start={start}，共找到 {len(items)} 部电影")

    for item in items:
        title = item.find("span", class_="title").text
        info = item.find("div", class_="bd").find("p").text.strip()
        year = info.split("\n")[1].strip().split("/")[0]
        rating = item.find("span", class_="rating_num").text

        movies.append({
            "title": title,
            "year": year,
            "rating": float(rating)
        })

    time.sleep(1)

print(f"\n🎉 总共抓取了 {len(movies)} 部电影")

df = pd.DataFrame(movies)
df.to_csv("new_douban_top250.csv", index=False, encoding="utf-8")
print("✅ 数据保存完成！")
