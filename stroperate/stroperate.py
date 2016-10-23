# list exercise

# names = "ZhangSan LiSi WangWu"

# names = []   #empty list

import copy
names = ['ZhangSan', 'LiSi', 'WangWu', 'LiuQi']
# print(names[0])
# print(names)

# for i in names:  # for loop print for each of names
#    print(i)

# print(names[1:3])  #split elements
# print(names[-1])   #pick the last one

# print(names[3])

# print(names[-2:]) #pick the last two elements

# print(names[:3])  #equal to names[0:3]

# names.append('QiQiao')  #default added to bottom
# print(names)

# names.insert(0,'JaiZheng')   #insert pos element

# print(names)
# names[2] = 'Doudou'
# print(names)


# names.remove('JaiZheng')    #order by ascii

# print(names)

# del names[0]               # delete variable
# print(names)

# names.pop()                # delete element default 0 pos
# print(names.index('ZhangSan'))

# print(names[names.index('ZhangSan')])

# names.reverse()
# names.sort()
name2 = []

names.append(['CAA','chen'])
names[4][1] = 'CHEN'


name2 = names.copy()  #shandow copy()

print(names,name2)

names[0] = 'JIAJIA'

# print(names)
#names.extend(name2)  # extend source


#print(names,name2)

#names = name2

#print(names,name2)

#print(names is name2)
#del names[0]

l = 5;
k = 6;

print(hex(id(l)))
print(hex(id(k)))

l = k       #单个变量之间的赋值等于 打印地址后为深拷贝原理 两个变量 指向为不同的内存地址

print(hex(id(names)))  #print the memory address of names  variable
print(hex(id(name2)))  #print the memory address of name2  variable

print(names,name2)

name2 = names #列表之间的赋值等于 打印地址后为引用效果 两个变量指向同一块内存地址

print(hex(id(names)))
print(hex(id(name2)))

for i in names:
    print((hex(id(i))),i)





#del name2
