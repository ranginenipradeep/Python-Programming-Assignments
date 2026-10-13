
# Get order amount and membership status from the user
amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").lower()

# Check whether the order amount is valid
if amount < 0 or amount > 100000:
    print("Invalid order amount")

# Give 15% discount for orders of ₹5000 or more
elif amount >= 5000:
    discount = amount * 15 / 100
    print("Eligible for 15% discount")

# Give 10% discount to members for orders of ₹2000 or more
elif membership == "yes" and amount >= 2000:
    discount = amount * 10 / 100
    print("Eligible for 10% discount")

# No discount for all other orders
else:
    discount = 0
    print("No discount")

# Display the bill only if the order amount is valid
if amount >= 0 and amount <= 100000:

    # Check whether the customer qualifies for a discount
    if amount >= 5000 or (membership == "yes" and amount >= 2000):
        print("Original amount: ₹", amount)
        print("Discount amount: ₹", discount)
        print("Final payable amount: ₹", amount - discount)

    # Display the bill when there is no discount
    else:
        print("Original amount: ₹", amount)
        print("Discount amount: ₹", discount)
        print("Final payable amount: ₹", amount)
