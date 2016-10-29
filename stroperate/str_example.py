
name = 'molin \tname'

#print(name.capitalize())  #cap high
#print(name.count("a"))
print(name.center(50,"-")) #将字符居中显示，两头填充指定的字符

print(name.endswith("caa"))#判断是否以指定字符结尾

print(name.expandtabs(tabsize=30))

print(name.find("name")) #查找查找子串，返回第一个匹配的下标

print("23hef".isalnum())#判断是否是数字和字母

print("abA".isalpha()) #判断是否是字母

print("0x23".isdecimal()) #判断是否是十进制

print("if".isidentifier())  #判断是否是合法的标识符

print("21".isnumeric())    #判断是整数

print("3.41".isnumeric())

print("3".isdigit())  #判断是否是整数

print("My Name Is".istitle()) #判断首字母是否大写

print("my name".isupper())  #判断是否是大写

print('+'.join(['1','2','3'])) #join参数为可迭代对象将填充字符查串填充至可迭代对象的每个元素之间

print(name.ljust(20,"＝"))  #保证输出字符个数为 20 个不够时在右边填充，填充字符

print(name.rjust(20,"="))   #保证所输出字符个数为20 个数不够在左边填充，填充字符

print("anan".upper())  #小写边大写

print("ANAN".lower()) #大写边小写

print("ehehe".strip("e")) #默认去除开头结尾的空格,如果不指定去除的字符，指定了则去除开头和结尾的指定字符

p = str.maketrans("abcdef","abcdef") #作映射

print("an".replace('a','A'))    #替换

print("caaa".rfind("h")) #匹配最后一个匹配的字符下标，失败返回 －1

print("chEn aNan".swapcase())  #大小写变换 大写变小写，小写边大写

print("ss".zfill(10)) #返回字符总长度为设置值不够用0填充









