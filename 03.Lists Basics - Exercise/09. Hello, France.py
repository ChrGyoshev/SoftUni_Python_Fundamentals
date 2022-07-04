item_prices = input().split("|")
budget = float(input())
all_clothes_prices = 0
profit =0
clothes = 50.00
shoes = 35.00
accessories = 20.50
new_list = []
for current in item_prices:
    type_clothes, price = current.split("->")
    price = float(price)
    if type_clothes == "Clothes" and price > clothes:
        continue
    elif type_clothes =="Shoes" and price > shoes:
        continue
    elif type_clothes == "Accessories" and price > accessories:
        continue
    if budget >= price:
        budget -= price
        all_clothes_prices += price
        price *= 1.4
        price = "{0:.2f}".format(price)
        new_list.append(price)

profit = sum(map(float,new_list)) - all_clothes_prices
ticket = budget + sum(map(float,new_list))
for i in new_list:
    print(i, end=" ")
print()
print(f"Profit: {profit:.2f}")
if ticket >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

