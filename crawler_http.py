#https://www.fx110.com.tw/
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.fx110.com.tw/')

if response.status_code == requests.codes.ok: #200
	# 以 BeautifulSoup 解析 HTML 程式碼
	soup = BeautifulSoup(response.text, 'html.parser')

	exchangeArr = soup.find_all("a", class_="list")
	for info in exchangeArr:
		currencyData = info.find('div', class_="currency")
		name = currencyData.find('p', class_="txt").text
		amount = currencyData.find('p', class_="amount").string

		print(name, amount)

	# print('test')
else:
	print('fail!')
