# -*- coding: UTF-8 -*-
# @Author  : wucha
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2024/3/17 23:08
# @Project : Request_Learn.py
# @File    : test_baidu.py
import requests

url_baidu = 'https://www.baidu.com/'
response = requests.get(url_baidu)

print(response.apparent_encoding)
response.encoding = response.apparent_encoding

# print(response.text)
# print(response.content)

session = requests.session()

session.get(url_baidu)

url = 'https://www.baidu.com/ssid=8990c4e3b5c4cdbcd4dac4c49d37/from=844b/s?word=pytest&ts=0&t_kt=0&ie=utf-8&rsv_iqid=11361260046489662591&rsv_t=e7bbXBBAon8EDf5cxcLim%252B9a9NejqAigESbkGJVLOO%252B8ANlNHBUr2KqGAg&sa=ib_d&ms=1&rsv_pq=11361260046489662591&rsv_sug4=1710688962822&tj=1&inputT=1710688971940&sugid=3170675134999&ss=100&rqid=11361260046489662591&rfrom=1040158w&rchannel=1040295a'
headers = {'word': 'pytest'}
response1 = session.get(url, headers=headers)
response1.encoding = response1.apparent_encoding
print(response1.content)
# print(response1.text)
