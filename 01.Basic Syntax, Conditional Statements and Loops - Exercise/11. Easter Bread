budget = float(input())
price_for_kg_flavor = float(input())
one_pack_eggs_price = price_for_kg_flavor * 0.75
one_l_milk_price = price_for_kg_flavor * 1.25
quarter_milk_price = one_l_milk_price * 0.25
one_loav_price = price_for_kg_flavor + quarter_milk_price + one_pack_eggs_price
loaves = 0
colored_eggs = 0
money_left = 0

while budget >= one_loav_price :
    budget -= one_loav_price
    loaves +=1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
