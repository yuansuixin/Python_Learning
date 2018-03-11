import requests
import json
import re

'''
爬取淘宝某商品的销量
'''
# 得到淘宝网页的文本
def open_url(keyword,page=1):
   # s:表示从第1个商品开始显示，由于1页是44个商品，
   # sort：表示按照销量排序
    payload = {'q':'零基础入门学习Python','s':str((page-1)*44),'sort':'sale-desc'}
    url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180102&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0Python&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest'

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    res = requests.get(url,timeout=60,params=payload,headers=headers)
    return res


# 获取列表页的所有商品
def get_items(res):
    # g_page_config = re.search(r'g_page_config = (.*?);\n',res.text)
    # page_config_json = json.loads(g_page_config.group(1))
    # print(g_page_config)
    with open('items.txt', 'r', encoding='utf-8') as f:
        g_page_config = re.search(r'g_page_config = (.*?);\n', f.read())
        # print(g_page_config)
        # print(g_page_config.group(1))
        page_config_json = json.loads(g_page_config.group(1))
    page_items = page_config_json['mods']['itemlist']['data']['auctions']

    results = []  # 整理出我们关注的信息，id 标题 连接  售价 销量和商家
    for each in page_items:
        dict1 = dict.fromkeys(('nid','title','detail_url','view_price','view_sales','nick'))
        dict1['nid'] = each['nid']
        dict1['title'] = each['title']
        dict1['detail_url'] = each['detail_url']
        dict1['view_price'] = each['view_price']
        dict1['view_sales'] = each['view_sales']
        dict1['nick'] = each['nick']

        results.append(dict1)
        return results


def count_sales(items):
    # 统计销量
    count= 0
    for each in items:
        if '小甲鱼' in each['title']:
            count += int(re.search(r'\d+',each['view_sales']).group())

    return count



def main():
    keyword= '零基础入门学习Python'

    length = 3
    total = 0

    for each in range(length):
        res = open_url(keyword,each+1)
        items = get_items(res)
        total += count_sales(items)

    print('总销量为：',total)


if __name__ == '__main__':
    main()

































