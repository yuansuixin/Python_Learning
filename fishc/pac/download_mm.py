import os
import urllib.request
from selenium import webdriver

driver = None
def open_url(url):
    driver.get(url)
    html=driver.page_source
    return html

def open_img_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
   
    return html

def save_img(folder,img_addr):
    for each in img_addr:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = open_img_url(each)
            f.write(img)
    
def get_now_page(url):
    html = open_url(url)
    #html = html.decode('utf-8')
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]

def get_img(url):
    html = open_url(url)
    #html = html.decode('utf-8')
    
    img_addr = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            
            print(a,b)
            img_addr.append(html[a+9:b+4])
        else :
            b = a +9
        a = html.find('img src=',b)
        
        
    for i in img_addr:
        print(i)
    #raise Exception('a')
    return img_addr

def download_mm(folder = 'OOXX',page = 10):
    os.mkdir(folder)
    os.chdir(folder)
    global driver
    driver = webdriver.PhantomJS()
    url = 'http://jandan.net/ooxx/'
    
    page_num = int(get_now_page(url))
    print(page_num)

    for i in range(page):
        page_num -=i
        page_url = url + 'page-' + str(page_num)
        img_addr = get_img(page_url)
        save_img(folder,img_addr)

if __name__ =='__main__':
    download_mm()
