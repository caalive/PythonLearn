#!/usr/bin/env python

#The Shopping car exercise use list

goodsList = ['1.Iphone      5800','2:Mac Pro     12000','3:Bike        700','4:Book        80']


salary = int(input("Input your salary:")) #input Balance

shoppingCar = []  #goods list default is empty

def printInfo():  #func print goods infomation
    print('goodsInfo     Price')
    for i in goodsList:
        print(i)

choice = 'C'  #default value

while True:
    if choice != 'B':  #go back here print goods info if choice not 'B'
        printInfo()    #print goods info
    choice = input("Choise Goods or input Q to exit:")
    if choice == 'Q':  #choice 'Q' to exit
        break
    elif(choice == '1'):
        if(salary < 5800):  #count balance
            print("Sorry your balance is not enough to buy it!")
            choice = input('Enter the B to goback or Q to exit:')
            if(choice == 'Q'):
                break         #exit
            elif(choice == "B"):
                printInfo()
                continue
        else:
            print('Successful added the goods to your shoppping car!')
            shoppingCar.append('Iphone')   #append goods to shopping car
            salary = salary - 5800
            print('You have %d Balance yet!'%salary)
    elif (choice == '2'):
        if (salary < 12000):
            print("Sorry your balance is not enough to buy it!")
            choice = input('Enter the B to goback or Q to exit:')
            if (choice == 'Q'):
                break
            elif (choice == "B"):
                printInfo()
                continue
        else:
            print('Successful added the goods to your shoppping car!')
            shoppingCar.append('Mac Pro')
            salary = salary - 12000
            print('You have %d Balance yet!' % salary)
    elif (choice == '3'):
        if (salary < 700):
            print("Sorry your balance is not enough to buy it!")
            choice = input('Enter the B to goback or Q to exit:')
            if (choice == 'Q'):
                break
            elif (choice == "B"):
                printInfo()
                continue
        else:
            print('Successful added the goods to your shoppping car!')
            shoppingCar.append('Bike')
            salary = salary - 700
            print('You have %d Balance yet!' % salary)

    elif (choice == '4'):
        if (salary < 80):
            print("Sorry your balance is not enough to buy it!")
            choice = input('Enter the B to goback or Q to exit:')
            if (choice == 'Q'):
                break
            elif (choice == "B"):
                printInfo()
                continue
        else:
            print('Successful added the goods to your shoppping car!')
            shoppingCar.append('Book')
            salary = salary - 80
            print('You have %d Balance yet!' % salary)

print('Your choice goods is:')   #print choise goods list
for i in shoppingCar:
    print(i)
print('Your Balance is %d'%salary)  #pint balance
print('Thank you,Bye,Bye!!')        #exit


