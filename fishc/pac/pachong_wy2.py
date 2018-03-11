"""
爬取网易云音乐上指定歌曲的精彩评论
"""

import requests
import json

# 获取到精彩评论
def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt','w',encoding='utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname']+':\n')
            f.write(each['content']+'\n\n')
            f.write('----------------------------------------------\n')

def get_comments(url):
    name_id = url.split('=')[1]
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
               'referer':'http://music.163.com/song?id=4466775'}
    res = requests.get(url,headers=headers)

    params='ttbEA7eEwh6khZka/zkFmj+XRHlHjsy5MZQITFtkmLxCMjTZslPCVoAqHZyfiKp+gnyh/dN+7r1ejzDHXDCEM8LTgsNRjLQhuwHf/Suc/pRX8ry0aQsShY6Yvhkh044mQ02Fz06zkDf8MQBZzYZBbcirGK6kgxMhgc8TPbop9AnP84MEIaYe5a+xwRvpKYM8'
    encSecKey='5da1b2816879dd2dc42eb9aa80143391f550bf78f0507e5f78699ed82329c7249d447d4bd0d31b357b68264e12e13b6c669816f1081de1cc1befe70801219b409459a7421b64cf6d2cdd652a79304a464a6f9d952a9343cb48947e0b7652035d168eebe0f38484ab5ca7428a12901c73702424a1f9a4d4f072007e59c0d5767d'
    data = {
        'params':params,
        'encSecKey':encSecKey
    }
    target_url ='http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
    res = requests.post(target_url,headers=headers,data=data)
    return res


def main():
    url = input('请输入连接地址：')
    res = get_comments(url)
    get_hot_comments(res)


if __name__ == '__main__':
    main()










