import random
print("***WELCOME TO NUMBER GUESSING GAME***")
print("I am thinking of a number between 1 and 100")
choose_label = input("Choose a difficulty. Type 'easy' or 'hard': ")
computer_guess = random.randint(1,100)

if choose_label == "easy":
    n = 10
else:
    choose_label == "hard"
    n = 5    

total_attempts = n
while total_attempts < n+1:
    print(f"You have {total_attempts} attempts remaining to guess the number.")
    total_attempts -= 1

    guess = int(input("Make a guess:  " ))
    if guess > computer_guess:
        print("Too high. \nGuess again.")
    elif guess < computer_guess:
        print("Too low. \nGuess Again.")
    elif guess == computer_guess:
        print("Congratulations!!You got it.")
        break
    if total_attempts == 0:
        print("You have no attempts remaining. You lose.")
        break        

     


