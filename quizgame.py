# Python quiz game

questions = ("How many elements are there in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What is the capital of Australia?: ",
             "Which company owns the Polo GTI?:",
             "Who owns M5 Competition?: ",)
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Canberra", "B. Wellington", "C. Melbourne", "D. Sydney"),
           ("A. Volkswagen", "B. Audi", "C. Mercedes", "D. Bentley"),
           ("A. BMW", "B. Toyota", "C. Mitshubishi", "D. Honda"),)

answers = ("C", "D", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print("The correct answer is: ", answers[question_num])
    question_num += 1

print("------------------------------------")
print("Your score is: ", score)
print("Your guesses: ", guesses)

print("------------------------------------")
print("Thank you for playing the quiz game!")
print("-------------Result-----------------")