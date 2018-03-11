
import requests
import re
from bs4 import BeautifulSoup

def main():
    url = 'http://www.dytt8.net/'
    res = requests.get(url,timeout=30)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text,'html.parser')
    L = soup.find_all('td',class_='inddline')
    # print(L)
    pat = r'《.*?》' # 获取书名号的内容
    mov = re.findall(pat,str(L))
    print(mov)
    with open('movies.txt','w',encoding='utf-8') as f:
        for each in mov:
            f.write(each+'\n')


    # print(soup.original_encoding)  # 查看bs4是否猜对了原文的编码格式
if __name__ == '__main__':
    main()







