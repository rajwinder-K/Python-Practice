from datetime import datetime 
balance = 5000
history = []
pin = "1234"
attempts = 3
def verify_pin():
    global attempts
    while attempts > 0:
        PIN = input("Enter PIN: ")
        if PIN == pin:
            print("Login Successful!")
            return True
        else: 
            attempts -= 1
            print(f"Remaining attempts: {attempts}")
    
    print("Too many incorrect PIN attempts.")
    print("Your account has been temporarily locked.")
    return False 

def ATM_Machine():
        global balance,history   
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")     
        try: 
            # Title banner
            print("=" *35)
            print("         ATM MENU")
            print("=" *35)
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Current Balance: {balance:.2f}")

            elif choice == 2:
                deposit = float(input("Enter the amount you want to deposit: "))
                if deposit > 0:
                    balance += deposit
                    history.append(f"[{current_time}]Deposited {deposit:.2f}")
                    print(f"{deposit:.2f} deposited successfully")
                    print(f"Current Balance: {balance:.2f}")
                    receipt = input("Do you want a receipt? (Y/N):").strip().upper()
                    if receipt == "Y":
                        print("=" *35)
                        print("         RECEIPT")
                        print("=" *35)
                        print("Transaction : Deposit")
                        print(f"Amount    :{deposit:.2f}")
                        print(f"Balance   :{balance:.2f}")
                        print("Thank you for using our ATM!")

                else:
                    print("Please enter a valid amount")

            elif choice == 3:
                withdrawal = float(input("Enter the amount you want to withdraw: "))
                if withdrawal > 0 and balance >= withdrawal:
                    balance -= withdrawal
                    history.append(f"[{current_time}]Withdrew {withdrawal:.2f}")
                    print(f"{withdrawal:.2f} withdrawn successfully")
                    print(f"Current Balance: {balance:.2f}")
                    receipt = input("Do you want a receipt? (Y/N):").strip().upper()
                    if receipt == "Y":
                        print("=" *35)
                        print("         RECEIPT")
                        print("=" *35)
                        print("Transaction : Withdraw")
                        print(f"Amount    :{withdrawal:.2f}")
                        print(f"Balance   :{balance:.2f}")
                        print("Thank you for using our ATM!")
                elif withdrawal > balance:
                    print("Insufficient balance")
                else:
                    print("Please enter a valid amount")
            elif choice == 4:
                if not history :
                    print("No transactions yet.")
                else:
                    print("Transaction History: ")
                    for index,transaction in enumerate(history,start=1):                        
                       print(f"{index}. {transaction}")
            elif choice == 5:
                print("Thank you for using our ATM.") 
                return False
            else:
                print("Invalid choice")
        except ValueError: 
            print("\nInvalid choice!") 
            print("Please enter valid number .\n")
        return True 
# Loop for multiple calculations
if verify_pin():    
    while True:
        if not ATM_Machine():
            break       
