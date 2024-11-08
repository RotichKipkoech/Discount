# Define the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user to input the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
