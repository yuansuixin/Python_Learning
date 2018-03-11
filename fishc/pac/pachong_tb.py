import requests
import json
import re

'''
爬取淘宝某商品的销量
'''
# 得到淘宝网页的文本
def open_url(keyword):
    payload = {'q':'零基础入门学习Python','sort':'sale-desc'}
    url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180102&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0Python&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
    res = requests.get(url,timeout=60,params=payload)
    return res


def main():
    keyword = input('请输入搜索的关键词:')
    res = open_url(keyword)

    with open('items.txt','w',encoding='utf-8') as f:
        f.write(res.text)


if __name__ == '__main__':
    main()















