command = input()
receipt = 0
final = 0
while not command == "special" and not command == "regular":
    price = float(command)
    if price <0:
        print("Invalid price!")
        command = input()
        continue
    else:
        receipt += price
    command = input()

if receipt <= 0:
    print("Invalid order!")
else:
    if command == "special":
        final = (receipt * 1.20) * 0.90
    else:
        final = receipt * 1.20
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {receipt:.2f}$\n"
          f"Taxes: {receipt * 0.20:.2f}$\n"
          f"-----------\n"
          f"Total price: {final:.2f}$")