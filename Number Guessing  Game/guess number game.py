import random
def play_game():
    print("Welcome to Guess the Number Game!")
    print("Choose Difficulty Level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–1000)")

    # Difficulty selection
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                secret_number = random.randint(1, 50)
                print("You chose Easy! Guess the number between 1 and 50.")
                break
            elif choice == 2:
                secret_number = random.randint(1, 100)
                print("You chose Medium! Guess the number between 1 and 100.")
                break
            elif choice == 3:
                secret_number = random.randint(1, 1000)
                print("You chose Hard! Guess the number between 1 and 1000.")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Oops! That wasn’t a valid number. Please enter 1, 2, or 3.")
    # Game loop
    count = 1
    while True :
        try:
            # Code that may raise an error
            number = int(input("Enter a number: ")) 
            print (f"Attempt:  {count}")
            print("You entered:", number)
            if number == secret_number :
                print(f"Congrats,you guessed it in {count} attempts.") 
                break          
            elif number > secret_number :
                print("Too High,try again!")
            else:
                print("Too Low,try again!")
            # Hint system
            if abs(number - secret_number) <= 10:
                print("Hint: You’re very close!")

            count+=1
            print("-----------------------")
        except ValueError:
            # Code that runs if an error occurs
            print("Oops! That wasn’t a valid number. Please try again.")
    print("\n-----------------------")
    print("Thanks for Playing\n")

# Replay option
while True:
    play_game()
    again = input("Do you want to play again? (yes/y or no/n): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Goodbye!")
        break
