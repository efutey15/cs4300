#Task 4: Functions and Duck Typing

def calculate_discount(price, discount):
    if isinstance(discount, int):
        amountDiscounted = price*(discount*0.01)
    else:
        amountDiscounted = price*discount
    finalPrice = price - amountDiscounted
    return finalPrice

#main
def main():
    initialPrice = input("Enter a price: ")
    discount = input("Enter a discount: ")

    #Calculate discount and print final price
    finalPrice = calculate_discount(initialPrice, discount)
    print(f"The price after the discount is {finalPrice}")