# -*- coding: UTF-8 -*-
# @Author  : wucha
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2024/3/17 23:08
# @Project : Request_Learn.py
# @File    : test_zhibo8.py

from commons.request_util import send_request


class TestApi:
    # 封装后不需要在单独建立session
    # sess = requests.session()
    url = 'https://www.zhibo8.com/'
    datas = {

    }

    def test_visit_webpage(self):
        res = send_request(method='get', url=TestApi.url, params=TestApi.datas)
        assert res.status_code == 200
        # 获取网页编码方式,这种方式有时不准确
        # res_encoding = res.encoding
        # print(res_encoding)

        # 获取网页编码方式,这种方式准确率高一些
        # res_encoding = res.apparent_encoding
        # print(res_encoding)

        # 通过header去判断网页编码方式，这种方式最准确，但有的网页响应头没有charset，会导致报错
        # res_encoding=res.headers.get('Content-Type').split('charset=')[1]
        # print(encoding_from_header)

        # 将网页内容按正确的编码样式解码
        # decoded_content = res.content.decode(res_encoding)
        # print(decoded_content)


if __name__ == '__main__':
    # noinspection PyArgumentList
    TestApi.test_visit_webpage()
