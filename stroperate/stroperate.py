# list exercise

# names = "ZhangSan LiSi WangWu"

# names = []   #empty list

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
name2 = [1, 2, 3, 4]

# print(names)
names.extend(name2)  # extend source

print(names)

del name2
