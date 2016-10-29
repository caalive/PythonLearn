
product_list = [('Iphone',5900),
                ('Mac Pro',12000),
                ('Coffee',50),
                ('Book',40)]

shopping_list = [];

def print_product_list():
    for index,item in enumerate(product_list):
        print(index,item)


def print_shopping_list():
    for item in shopping_list:
        print(item)


salary = input("Input your salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        print_product_list()
        user_choice = input("选择你要购买的商品编号或按下 q 退出>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >=0 and user_choice < len(product_list):
                if salary < int(product_list[user_choice][1]):
                    print("Yor salary is not enough to buy it!!")
                else:
                    item = product_list[user_choice]
                    shopping_list.append(item)
                   # print("Added %s to your shopping cart!!"%product_list[user_choice])
                    salary -= item[1]
                    print("Added %s to your shopping cart,Your current balanace is \033[31;1m%s\033[0m"%(item,salary))

            else:
                print("could not find code [%s] product"%user_choice)

        elif(user_choice == 'q'):
            print("-------------------ShoppingList-------------------")
            print_shopping_list()
            print("Your current balanace is \033[31;1m%s\033[0m" %(salary))
            exit()
        else:
            print("Invalid input!!")





