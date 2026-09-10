units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 2
elif units <= 200:
    rate = 3
elif units <= 300:
    rate = 5
else:
    rate = 7

bill = units * rate

print("Total Electricity Bill: ₹", bill)