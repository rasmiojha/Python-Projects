foods=[]
prices=[]
total=0

while True:
    item = input("Enter items to buy (q to quite) :").strip()
    if item.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the Price of the {item}: $ "))
        foods.append(item)
        prices.append(price)
    
print("-------Your shopping list is----------------")

for food in foods:
    print(food,end = " ")

for price in prices:
    total += price
    
print()
print(f"Total price is : ${total}")