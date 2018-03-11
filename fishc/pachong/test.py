

import urllib.request
response = urllib.request.urlopen('http://www.fishc.com')
html = response.read()
print(html)  # 读出来的是二进制数据，我们可以对其进行解码操作
html = html.decode('utf-8')
print(html)













