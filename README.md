📚 Douban Movie Analyzer

这是我的学习项目，用于记录第一次上传 GitHub 的过程，以及学习编写网页爬虫的实践。

🎯 项目简介

本项目的目标是通过 Python 爬虫爬取 豆瓣电影 Top250 的电影数据，包括电影名称、上映年份和评分等信息，并对数据进行可视化分析。

🛠️ 使用技术
	•	Python 3
	•	requests
	•	BeautifulSoup
	•	pandas
	•	matplotlib

🧩 实现功能
	•	自动爬取豆瓣 Top250 电影的基础信息
	•	将数据保存为 CSV 文件
	•	对不同年代高分电影数量进行分析

🧪 运行方式

# 在项目目录下运行
python scrape_douban.py

# 执行数据分析（举例）
python analyze_by_decade.py

🔍 TODO
	•	更丰富的数据字段（导演、类型等）
	•	多线程加速爬取
	•	图表美化与交互性分析
