import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

movies = []

for start in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={start}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    for item in soup.find_all("div", class_="item"):
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

df = pd.DataFrame(movies)
df.to_csv("douban_top250.csv", index=False, encoding="utf-8")
print("数据保存完成！")
