# Age calculator
import datetime
# Ask user for birth year
try:
    birth_year = int(input("Enter your birth year:  ")) 
    current_year = datetime.datetime.now().year
    # calculate age
    age = current_year - birth_year
    if age < 0:
        print("Birth Year cannot be in the future.")
    else:
        print(f"Birth Year    : {birth_year}")
        print(f"Current Year  : {current_year}")
        print(f"Your age is   : {age}")
except ValueError:
    print("Please enter a valid number.") 
