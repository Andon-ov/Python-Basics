square_meters_of_landscaping = float(input())
price_for_the_whole_yard = square_meters_of_landscaping * 7.61
discount = price_for_the_whole_yard * 0.18
final_price = price_for_the_whole_yard - discount

print(f"The final price is:{final_price} lv.")
print(f"The discount is: {discount} lv.")