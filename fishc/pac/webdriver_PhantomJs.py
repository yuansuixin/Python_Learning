
from selenium import webdriver

'''
爬取淘宝某商品的销量,
'''


driver = webdriver.PhantomJS()
driver.get(r'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180102&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0Python&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest')
data = driver.page_source # 获取网页文本
with open('taobao.txt','w',encoding='utf-8') as f:
    f.write(data)
print('good')








