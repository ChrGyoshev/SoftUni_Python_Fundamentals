command = input()
products = {}

while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["quantity"] += quantity
        products[product]["price"] = price

    command = input()


for key, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{key} -> {total_price:.2f}")
