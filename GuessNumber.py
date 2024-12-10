import random

def number_guessing_game():
    print("Welcome to the number guessing game!")

    difficulty_level = input("Enter a difficulty level: easy, medium or hard: ").lower()
    if difficulty_level == "easy":
        target_number = random.randint(1, 50)
        max_attempts = 5
    elif difficulty_level == "medium":
        target_number = random.randint(1, 100)
        max_attempts = 5
    else:
        target_number = random.randint(1, 200)
        max_attempts = 5

    print(f"You have chosen {difficulty_level} mode. You get {max_attempts} attempts on this mode to guess the number!")

    attempts = 0

    while attempts < max_attempts:
        try:
    
            user_guess = int(input("Guess a number within your range: "))
            attempts += 1

            if user_guess == target_number:
                print(f"Congratulations, you just got the correct number {target_number} in {attempts} attempts.")
            elif user_guess < target_number:
                print(f"Too low, try again.")
            else:
                print(f"Too high, try again.")       
            
        except ValueError:
            print("Enter a valid number.")
            continue
    if attempts == max_attempts and user_guess != target_number:
        print(f"Game over! You have used all {max_attempts} attempts. The correct number is {target_number}.")

number_guessing_game()

                 

