import requests
import json
from bs4 import BeautifulSoup

"""
豆瓣top250电影的名字

"""
def main():
    url = r'https://movie.douban.com/top250'
    res = requests.get(url,timeout=30)
    soup = BeautifulSoup(res.text,'lxml')
    div_list = soup.find_all('div',{'class':'hd'})
    for each in div_list:
        print(each.a.span.text)


if __name__ == '__main__':
    main()












