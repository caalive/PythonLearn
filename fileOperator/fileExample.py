

#data = open("yesterday.txt").read()  #
#print(data)

'''
f = open("yesterday.txt",'r',encoding='utf-8') #文件句柄 文件内存对象

data = f.read() #使用read函数读取时文件指针会移动到文件末尾

f.seek(0,0) #重新移动文件指针至起始位置，重新赋值给data2

data2 = f.read()

print(data)

print('-------------data2-------------')
print(data2)
print('-------------data2-------------')

f.close()
'''

f = open("yesterday.txt",'a',encoding='utf-8')  # w 写模式打开文件，先清除文件内容再写入，文件明不存在则创建
                                                # r 读模式打开文件
f.write("yeaterday when i was young,\n")        # a 追加模式打开文件

f.write("yesterday when,\n")

f.close()












