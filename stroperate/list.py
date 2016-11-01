info  = {'stu1':'ca',
         'stu2':'cb',
         'stu3':'cc'}

print(info)

#info.pop('stu1')
#print(info)

print(info.get('stu4'))

print('stu3' in info)

print(info.values())

g = dict.fromkeys([1,2,3],{'name':'molin'})

print(g)

g[2]['name'] = 'john'

print(g)


for k,v in g.items():
    print(k,v)

for i in info:
    print(i,info[i])







