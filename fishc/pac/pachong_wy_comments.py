'''
爬网易云音乐上某歌曲的评论
'''

import requests
from bs4 import BeautifulSoup





def main():
    url = 'http://music.163.com/#/song?id=526464293'
    res = requests.get(url,timeout=30)
    soup = BeautifulSoup(res.text,'lxml')
    div_list = soup.find_all('div',class_='cnt f-brk')
    for each in div_list:
        print(each.a.text,end=':')
        print(each.text)
        print()





if __name__ == '__main__':
    main()




















