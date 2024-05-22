menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
    }
print("welcome to my python resturent")
print("pizza: RS70\nPasta: Rs50\nBurger: RS60\n Salad:Rs60\ncoffee: Rs90\n")

order_total=40

item_1=input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]  
    print(f" your item {item_1} has been added to your order")
    print("the total amount of items to pay is {order_total}")
    
else:
    print(f"ordered item{item_1} is not available yet|")
    
another_order=input("do you want to add another item?(yes/no)")
if another_order == "yes":
          item_2 =input("enter the name of second item = ")
          if item_2 in menu:
             order_total += menu[item_2]
             print(f" Item {item_2} has been  added to order")
          else:
              print(" ordered item  {item_2} is not available")
              print("the total amount of items to pay is {order_total}")
another_order=input("do you want to add another item?(yes/no)")
if another_order == "yes":
    item_3 =input("enter the name to add of second item = ")
    if item_2 in menu:
        order_total += menu[item_3]
        print(f" item {item_3} has been added to order")
        print("the total amount of items  to pay is {order_total}")
 
    else:
         print("ordered item  {item_3} is not available")
              
          
          
        

