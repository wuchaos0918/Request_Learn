# -*- coding: UTF-8 -*-
# @Author  : wucha
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2024/3/17 22:44
# @Project : Request_Learn.py
# @File    : test_bilibili.py
import requests

url = 'https://www.bilibili.com/'
response = requests.get(url)

# 使用response的encoding、apparent_encoding，得到网页的编码格式。
# encoding是从header中去提取，而apparent_encoding是从网页源码去解析。
# apparent_encoding得到的结果更准确。
print(response.encoding)
print(response.apparent_encoding)

# 1.手动在代码中指定文本编码格式为UTF-8
# response.encoding = 'utf-8'

# 2.在代码中指定文本编码格式为网页的编码格式
response.encoding=response.apparent_encoding

# 打印网页内容
print(response.text)
print(response.content)
