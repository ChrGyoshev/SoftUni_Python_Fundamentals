import re
pattern = r"(^|(?<=\s))@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
barcode_count = int(input())

for barcodes in range(barcode_count):
    current_command = input()
    match = re.match(pattern, current_command)
    if match:
        product_group = ''
        for el in current_command:
            if el.isdigit():
                product_group += el
        if product_group =="" :
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

