food_quantity_g = float(input()) * 1000
quantity_of_hay_g = float(input()) * 1000
quantity_cover_g = float(input()) * 1000
pig_weight_g = float(input()) * 1000
is_failed = False
for days in range(1,31):
    food_quantity_g -= 300
    if days % 2 == 0:
        quantity_of_hay_g -= (food_quantity_g * 0.05)
    if days % 3 == 0:
        quantity_cover_g -= (pig_weight_g/3)
    if food_quantity_g <= 0 or quantity_of_hay_g <= 0 or quantity_cover_g <= 0:
        is_failed = True
        break
if is_failed:
    print(f'Merry must go to the pet store!')
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity_g/1000:.2f}, Hay: {quantity_of_hay_g/1000:.2f}, Cover: {quantity_cover_g/1000:.2f}.")

