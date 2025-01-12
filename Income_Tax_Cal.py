def calculate_tax(income):
    tax = 0

    # Income tax slabs and rates
    if income <= 250000:
        tax = 0  # No tax for income up to ₹2.5 lakh
    elif income <= 500000:
        tax = (income - 250000) * 0.05  # 5% tax for income between ₹2.5 lakh to ₹5 lakh
    elif income <= 1000000:
        tax = (250000 * 0.05)  # 5% tax for the first ₹2.5 lakh
        tax += (income - 500000) * 0.20  # 20% tax for income between ₹5 lakh to ₹10 lakh
    else:
        tax = (250000 * 0.05)  # 5% tax for the first ₹2.5 lakh
        tax += (500000 * 0.20)  # 20% tax for the next ₹5 lakh
        tax += (income - 1000000) * 0.30  # 30% tax for income above ₹10 lakh

    return tax


def main():
    # Take income input from the user
    income = int(input("Enter your Income: "))
    
    # Calculate the tax based on the income
    tax = calculate_tax(income)

    # Output the calculated tax
    print(f"Tax is: ₹{int(tax)}")


if __name__ == "__main__":
    main()
