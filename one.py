order_amount = float(input("Enter order amount: ₹"))

if order_amount >= 2000:
    delivery_charge = 0
elif order_amount >= 1000:
    delivery_charge = 50
else:
    delivery_charge = 100

final_amount = order_amount + delivery_charge

print("Delivery Charge: ₹", delivery_charge)
print("Final Amount: ₹", final_amount)