"""
爬取网易云音乐上指定歌曲的精彩评论
"""

import requests


def get_url(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    res = requests.get(url,headers=headers)
    return res


def main():
    url = input('请输入连接地址：')
    res = get_url(url)

    with open('res.txt','w',encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    main()










