from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar
def Age_calculator():
        try: 
            # Title banner
            print("=" *35)
            print("         AGE CALCULATOR")
            print("=" *35)

            # Input date of birth
            dob = input("Enter your DOB (DD-MM-YYYY): ")
            birth_datetime = datetime.strptime(dob, "%d-%m-%Y")
            current_datetime = datetime.now()

            # Difference in days
            difference = current_datetime - birth_datetime
            total_days = difference.days
            total_seconds = difference.total_seconds()
            total_weeks = total_days // 7
            total_hours = int(total_seconds // 3600)
            total_minutes = int(total_seconds // 60)

            # Calculate age using relativedelta
            age = relativedelta(current_datetime,birth_datetime)
            total_months = (age.years *12) + age.months
   
            # Birthday check  
            if current_datetime.month == birth_datetime.month and current_datetime.day == birth_datetime.day:
                 print("🎉Happy Birthday!🎂") 

            # Next birthday calculation
            next_birthday = birth_datetime.replace(year = current_datetime.year)
            if current_datetime > next_birthday:
                 next_birthday = birth_datetime.replace(year = current_datetime.year + 1)
            days_left = (next_birthday - current_datetime).days

            # Day of week of birth
            day_of_week = birth_datetime.strftime("%A")

            # Leap year check
            is_leap = calendar.isleap(birth_datetime.year)

            # Age Category determination
            if age.years < 13:
                category = "Child"
            elif 13 <= age.years <= 19:
                category = "Teenager"               
            elif 20 <= age.years <= 59:
                category = "Adult"     
            else:
                category = "Senior Citizen"

            # Future age calculation    
            future_year_input = input("Enter future year (press Enter to skip): ")
            future_age_text = ""   
            if future_year_input:
                future_year = int(future_year_input)
                future_age = future_year - birth_datetime.year
                future_age_text = f"Age in {future_year} : {future_age} years"

            # Output sections
            print()
            print("Personal Information")
            print("-" *35)
            print(f"Date of Birth : {birth_datetime.strftime('%d-%m-%Y')}")
            print(f"Current Date  : {current_datetime.strftime('%d-%m-%Y')}")
            print(f"Day of Birth  : {day_of_week}")
            print()

            print("Age Details")
            print("-" *35)
            print(f"Exact Age     : {age.years} years, {age.months} months, {age.days} days")
            print(f"Total Months  : {total_months} months")
            print(f"Total Days    : {total_days} days")
            print(f"Total Weeks   : {total_weeks} weeks")
            print(f"Total Hours   : {total_hours} hours")
            print(f"Total Minutes : {total_minutes} minutes")
            print(f"Days until next birthday : {days_left} days")
            print()

            print("Birthday")
            print("-" *35)
            print(f"Next Birthday : {next_birthday.strftime('%d-%m-%Y')}")
            print(f"Days Left     : {days_left}")
            print()

            print("Other Information")
            print("-" *35)
            print(f"Leap Year     : {'Yes' if is_leap else 'No'}")
            print(f"Age Category  : {category}")
            if future_age_text:
                print(future_age_text)
            print()
                
            print("=" *35)
            print("Thank you for using  Age Calculator!")
            print("=" *35)
        except ValueError: 
            print("\nInvalid date!") 
            print("Please enter DOB in DD-MM-YYYY format.\n") 

# Loop for multiple calculations
while True:
    Age_calculator()
    
    choice = input("\nDo you want to calculate another age? (yes/y or no/n): ").strip().lower()
    if choice not in ["yes", "y"]:
        print("\nThank you for using the Age Calculator!")
        print("Have a great day!")
        break
    
