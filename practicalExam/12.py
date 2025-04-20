# Program to convert U.S. dollars to Indian rupees.

usd = float(input("Enter the amount in USD to convert to INR: "))

usdToInr = lambda usd : usd * 85.39

print(f"{usd} USD is equal to {usdToInr(usd)} INR")