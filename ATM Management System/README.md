# ATM Machine (Python Project)
A beginner‑friendly Python program that simulates an ATM machine.
It allows users to securely log in with a PIN, check their balance, deposit money, withdraw money, and view transaction history — all with a clean console interface.
# Features
 - PIN Verification with limited attempts (account locks after 3 wrong tries).
 - Check Balance anytime.
 - Deposit Money with optional receipt printing.
 - Withdraw Money with balance validation and receipt option.
 - Transaction History to track deposits and withdrawals with timestamps.
 - Exit Option to safely end the session.
# How It Works
```text
Run the program.
Enter your PIN (1234 by default).
Choose from the ATM menu:
1 → Check Balance
2 → Deposit Money
3 → Withdraw Money
4 → View Transaction History
5 → Exit
```
# Example 
## Output 1 :
```text
Enter PIN: 123
Remaining attempts: 2
Enter PIN: 1245
Remaining attempts: 1
Enter PIN: 12
Remaining attempts: 0
Too many incorrect PIN attempts.
Your account has been temporarily locked.
```
## Output 2 :
```text
Enter PIN: 1234
Login Successful!
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 1
Current Balance: 5000.00
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 2
Enter the amount you want to deposit: 5000
5000.00 deposited successfully
Current Balance: 10000.00
Do you want a receipt? (Y/N):Y
===================================
         RECEIPT
===================================
Transaction : Deposit
Amount    :5000.00
Balance   :10000.00
Thank you for using our ATM!
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 3
Enter the amount you want to withdraw: 2000
2000.00 withdrawn successfully
Current Balance: 8000.00
Do you want a receipt? (Y/N):Y
===================================
         RECEIPT
===================================
Transaction : Withdraw
Amount    :2000.00
Balance   :8000.00
Thank you for using our ATM!
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 1
Current Balance: 8000.00
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 4
Transaction History: 
1. [06-07-2026 05:11 PM]Deposited 5000.00
2. [06-07-2026 05:11 PM]Withdrew 2000.00
===================================
         ATM MENU
===================================
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 5
Thank you for using our ATM.
```
## Why This Project?
- Great for Python beginners to practice loops, conditionals, functions, and error handling.

- Demonstrates real‑world logic like PIN verification and transaction tracking.

- Can be extended with features like multiple accounts, interest calculation, or file storage.
