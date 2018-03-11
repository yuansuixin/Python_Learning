import pickle  # 导入泡菜模块

my_list = [123, 3.14, '小甲鱼', ['another list']]
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)  # 将文件存储
pickle_file.close()

# 使用load读取
pickle_file = open('my_list.pkl','rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)



