import requests

url = 'http://www.ip.cn/index.php?ip='
ip = input('请输入您要查询的IP：')

try:
    r = requests.get(url+ip)
    r.raise_for_status()  # 判断是否爬取成功
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')



