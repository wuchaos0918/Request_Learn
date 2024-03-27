#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2024-3-27 16:24
# @Project : Request_Learn.py
# @File    : request_util.py
# ______________________________
import requests


# 封装后，统一发送请求
def send_request(**kwargs):
    res = RequestUtil.sess.request(**kwargs)
    res_encoding = res.apparent_encoding
    print(res_encoding)
    decoded_content = res.content.decode(res_encoding)
    print(decoded_content)
    # 为了打印以上内容，return语句必须放最后
    return res


class RequestUtil:
    sess = requests.session()
