import urllib.request

#urlopen里面的data参数如果赋值了就使用POST方式提交，如果没有赋值就是用GET方式提交
response = urllib.request.urlopen('http://placekitten.com/200/200?image=13')
#response = urllib.request.Request('http://placekitten.com/200/200?image=13')  和上句中的功能一致

cat_img = response.read()

with open('cat_200.jpg','wb') as f:
    f.write(cat_img)


print(response.geturl())  # 获取访问的具体的连接地址
print(response.info())  # HTTPMessage对象，包含了远程服务器的信息
print(response.getcode())  # http的状态，正常响应200







