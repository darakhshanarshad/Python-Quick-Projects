#simple Bill calculator:
item = (input("enter item: "))
price = float(input("enter price: "))
quantity = int(input("enter quantity: "))

print("     Data     ")
print("-" * 20)
print(f"Item: {item}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")


print("-" *20)
print("    Bill    ")
original_price = price * quantity
print(f"price: {original_price}")

discount =  3 * original_price / 100
print(f"discount: {discount}")

final_price = original_price - discount
print(f"final price: {final_price}")