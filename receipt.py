# Class Exercise

product = []
quantity = []
price = []
total = []
bill = 0
shop = 'yes'
counter = 1

while 'yes':
    product_name = input("What are you buying? ")
    product.append(product_name)

    quantity_ = int(input("How many are you buying? "))
    quantity.append(quantity_)

    amount = int(input("Enter price: "))
    price.append(amount)

    total_price = amount * quantity_
    total.append(total_price)
    bill += total_price

    shop = input("Do you want to keep shopping? ")
    if shop == 'no':
        break

print("""************************************
Florence & Sons Group of Company
312 Herbert Macaulay way, Sabo, Yaba
07014014017 asherflo@yahoo.com
************************************""")
print("Product  Quantity    Price   Total")
for i in product:
    print(f"{product}: {quantity} {price} {total}")
print("""************************************
Thanks for your patronage
************************************""")
