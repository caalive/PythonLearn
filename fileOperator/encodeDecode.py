#-*- coding:utf-8 -*-   #文件编码

import sys
print(sys.getdefaultencoding())

str = "你好,GBK"   #python3 字符串默认编码为utf-8,想转换为别的 字符集编码 直接使用encode('')函数转换即可s

print(str.encode('gbk'))
print(str.encode('utf-8'))
print(str.encode('utf-8').decode('utf-8').encode('gb2312'))  #utf-8转换为gb2312

print(str)




