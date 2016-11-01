list_1 = [1,2,3,4,5,5,6,7]

list_1 = set(list_1)

print(list_1,type(list_1))


list_2 = [1,2,39,7]

list_3 = set([1,2])

#intersection  交集   &  符号表示
#union 并集           |  符号表示
#difference  差集     -  符号表示
#issubset   子集
#issuperset    父集

# ^ 尖括号表示对称差集


print(list_1.intersection(list_2))

print(list_1.union(list_2))

print(list_1.difference(list_2))

print(list_1.issubset(list_2))

print(list_1.issuperset(list_3))

print(list_1.isdisjoint(list_3))


# x in s  判断x 是否在s(str,list,dict,set)中通用测试方法