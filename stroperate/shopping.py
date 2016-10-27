

product_list = [('Iphone',5800),         #product info use list
                ('Mac Pro',9800),
                ('Bike',800),
                ('Watch',10600),
                ('Coffee',30),
                ('Book',50)]
salary = input("Input your salary:")    #input user salary

shopping_list = []                      #hold user user choice products

def print_Producet_list():              #define a function to print product info about product_list
    #for item in product_list:
    #    print(product_list.index(item),item)
    for index,item in enumerate(product_list):  # enumerate out index and item must be iteration
        print(index,item)

def shopping_Product_list():
    for index,item in enumerate(shopping_list):
        print(index,item)


if salary.isdigit():                    #check if isdigit
    salary = int(salary)                #convert to int type
    while True:                         #while loop
        print_Producet_list()           #call print_Product_list function
        user_choice = input("选择要买的商品>>:")
        if user_choice.isdigit():       #chck value
            user_choice = int(user_choice)
            if user_choice >= 0 and user_choice < len(product_list):
                product_item = product_list[user_choice]   #use user input index find product_list item
                if product_item[1] <= salary:              #pick up money
                    shopping_list.append(product_item)     #append item to shopping_list list
                    salary -= product_item[1]              #calc salary balance
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m"%(product_item,salary))
                else:
                    print("\033[41;1m你的余额不足只有[%s]元,无法购买!!\033[0m"%salary)
            else:
                print('product code [%s] not exist!!'%user_choice)
        elif user_choice == 'q':                                     #press 'q' goback
            print('--------------shopping list-------------')        #print
            shopping_Product_list()                                  #print already buied product info
            print('You current balance:\033[31;1m%s\033[0m'%salary)  #print current balance
            exit()
        else:
            print('invalid option!!')                                # not 'q' print error message














