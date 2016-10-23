#!/usr/bin/env python3
#f = open('userinfo.txt','r')

userinfo = []   #save name and password from read file

for line in open('userinfo.txt','r'):
    temp = line.split("=")[1]        #split with "=" by by the foramt
    temp = temp.split(":")
    line = (temp[0], temp[1].strip('\n'))
    userinfo.append(line)            #append to userinfo

loop = 3     # loop val

while loop > 0:
    name = input("Please input your username:")
    password = input("Please input yor password:")
    for check in userinfo:
        if(check[0] == name and check[1] == password):  #check username and password with input
            print("Welcome %s Login!!!"%name)   #login success
            loop = 0;
            break
    if(loop != 0 and loop != 1): #message remind
        print("Wrong username or password,you have %d times yet"%(loop - 1))
    loop -= 1
if(loop == 0): #exit
    print("you tried over 3 times,latter mintues try again!!!")





