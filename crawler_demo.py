# doc: https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/
# 引入 Beautiful Soup 模組
from bs4 import BeautifulSoup

# 原始 HTML 程式碼
html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

# 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

# title_tag = soup.title.string #.text
# print(title_tag)

# 所有的超連結
# a_tags = soup.find_all('a')
# for tag in a_tags:
#   # 輸出超連結的文字
#   print(tag.get('href'))

# 搜尋所有超連結與粗體字
# tags = soup.find_all(["a", "b"])
# print(tags)
# for tag in tags:
# 	if not tag.get('id') is None:
# 		print(tag.get('id'))

# 限制搜尋結果數量
# tags = soup.find_all(["a", "b"], limit=2)
# for tag in tags:
# 	print(tag.string)

# 只抓出第一個符合條件的節點
# a_tag = soup.find("a")
# print(a_tag)

# a_tag = soup.find("a", id="link1", href="/my_link1")
# print(a_tag)

# 不使用遞迴搜尋，僅尋找次一層的子節點
# titles = soup.html.find_all("title", recursive=False)
# print(titles)
