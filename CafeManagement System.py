#Define Menu of The Restaurant

menu ={
    'tea':10,
    "coffee":15,
    "pizza": 50,
    "cold Coffee":35,
    "burger": 70,
    "sandwish":30
}
#Greet
print("Welcome To PYTHON  Restaurant ")
print("Tea :10rs \nHot Coffee :15rs\nPizza : 50rs\nCold Coffee : 35rs\nBurger : 70rs\nSandWish: 30rs ")

order_Total = 0

item_1 =input("Enter the Name of item you want to order = ")

if item_1 in menu:
    order_Total += menu[item_1]
    print(f"Your item {item_1} has been added to your order ")

else:
    print(f"Ordered item {item_1} not available yet")

another_order = input("Do you want to add another item ? (Yes / No)")

if another_order =="yes":
    item_2 =input("Enter the name of Second item = ")


    if item_2 in menu :
        order_Total += menu [item_2]
        print(f"Item {item_2} has been added to order")
    else :
        print(f"Ordered item {item_2} is not Available Yet ")
print(f"The Total amount of items to pay is = {order_Total}")


