from datetime import datetime
def Age_calculator():
        try: 
            print("=" *35)
            print("         AGE CALCULATOR")
            print("=" *35)     
            
            dob = input("Enter your DOB (DD-MM-YYYY): ")
            birth_date = datetime.strptime(dob, "%d-%m-%Y").date()
            current_date = datetime.now().date()
            difference = current_date - birth_date
            total_days = difference.days

            years = current_date.year - birth_date.year

            if (current_date.month < birth_date.month) or (current_date.month == birth_date.month and current_date.day < birth_date.day):
                years -= 1

            print()
            print(f"Date of Birth : {birth_date.strftime('%d-%m-%Y')}")
            print(f"Current Date  : {current_date.strftime('%d-%m-%Y')}")
            print()

            print(f"Your age is   : {years} years" )
            print(f"Days lived    : {total_days} days" )
            print()

            print("=" *35)
            print("Thank you for using  Age Calculator!")
            print("=" *35)
        except ValueError: 
            print("\nInvalid date!") 
            print("Please enter DOB in DD-MM-YYYY format.\n") 
while True:
    Age_calculator()
    
    choice = input("\nDo you want to calculate another age? (yes/y or no/n): ").strip().lower()
    if choice not in ["yes", "y"]:
        print("\nThank you for using the Age Calculator!")
        print("Have a great day!")
        break
    
