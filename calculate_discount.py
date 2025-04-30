def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    else:
        return price 


original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"The final price after a {discount}% discount is: {final_price:.2f}")
else:
    print(f"The price remains the same: {original_price:.2f}")
    