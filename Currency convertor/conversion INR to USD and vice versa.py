# Currency Convertor 
print("1. INR to USD")
print("2. USD to INR")

usd_to_inr = 86

choice = int(input("Enter your choice: "))
if(choice == 1):
#INR to USD 
    INR = float(input("Enter Amount in INR: "))
    usd = INR / usd_to_inr 
    print(f"{INR:.2f} rupee = ${usd:.2f}")
else:  
# USD to INR 
    USD = float(input("Enter Amount in USD: "))
    inr= USD * usd_to_inr 
    print(f"${USD:.2f} = {inr:.2f} rupee")
