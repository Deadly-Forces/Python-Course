# number guessing game
import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
print("Welcome to the number guessing game!")
print(f"Select a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Enter your guess: ")
    try:
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! Try Again!")
        elif guess > answer:
            print("Too high! Try Again!")
        else:
            print("You got it!")
            print(f"The answer was {answer}.")
            print(f"It took you {guesses} guesses.")
            is_running = False    
    except ValueError:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}.")

        

# print(answer)