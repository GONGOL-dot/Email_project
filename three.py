purchase_amount = float(input("Enter purchase amount: ₹"))

if purchase_amount >= 5000:
    discount = 20
elif purchase_amount >= 3000:
    discount = 10
elif purchase_amount >= 1000:
    discount = 5
else:
    discount = 0

discount_amount = purchase_amount * discount / 100
final_amount = purchase_amount - discount_amount

print("Discount:", discount, "%")
print("Discount Amount: ₹", discount_amount)
print("Final Amount: ₹", final_amount)