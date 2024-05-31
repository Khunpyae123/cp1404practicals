"""
Shop Calculator
Pseudocode
item_count=0
total_price=0
get items
while items<0
    display Ivalid input
    get items
for range in items
    get price
    if price >0
        item_count= item_count + 1
        total_price= total_price + 1
        if total_price> 100
            discount= total_price* 0.1
            total_price= total_price - discount
        else
            display Invalid price
display items and total_price
"""

item_count=0
total_price=0
items=int(input("Number of items: "))
while items < 0:
    print("Invalid input")
    items = int(input("Number of items: "))
for i in range(0, items):
    price = float(input("Price of item: "))
    if price >0:
        item_count += 1
        total_price += price
        if total_price> 100:
            discount= total_price* 0.1
            total_price= total_price - discount
    else:
        print("Invalid price")
print(f"Total price for {item_count} items is ${total_price:,.2f}")