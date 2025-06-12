import pandas as pd

# 读取爬虫得到的 CSV 文件
df = pd.read_csv("douban_top250.csv")

# 假设你的年份列叫 '年份'，有些可能包含括号、字符串，先清洗
# 比如 '(1994)' -> 1994，可能需要用正则提取
df['year'] = df['year'].astype(str).str.extract(r'(\d{4})').dropna().astype(int)

# 创建“年代”列：如 1994 → 1990s
df['年代'] = (df['year'] // 10 * 10).astype(str) + 's'

# 按年代统计电影数量
decade_counts = df['年代'].value_counts().sort_index()

# 打印结果
print("各年代电影数量分布：")
print(decade_counts)
