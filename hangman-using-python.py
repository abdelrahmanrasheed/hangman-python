import random

words = ("laptop","touchscreen","whiteboard","touchpad","mousepad","projector","trackball")
guess = random.choice(words).upper()

# Operators to collect letters users entered that eventually is distrbuted accordingly in (correct) to collect correct letter from user
# (incorrectguesses) to collect incorrect letters from users that eventually when it exceeds the maximum length the user loses the game :(
correct = []
incorrectguesses = []

def program():
    # here if the user enters a letter that the program checks if it is correct, the program adds it to correct operator
    # so here if it is correct the program displays the letter along with dashes, else it displays empty dashes and the incorrectguesses length increases
    for i in guess:
        if i in correct:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print ("\n")

def main():
    # here is the main program, the belly of the beast. A while loop that continusly displays enter message to the user everytime he/she enters a letter
    # whether the letter is right or wrong, also checks if the letter was entered before, checks if it is more than one letter, and if the user didn't type any
    while True:
        userguess = input("Please Enter one letter:")
        userguess = userguess.upper()
        if userguess in correct or userguess in incorrectguesses:
            print("You have already guessed", userguess,"sorry")
        elif len(userguess) > 1:
            print("Please enter one letter only")
        elif len(guess) == 0:
            print("Please type a letter")
        else:
            break
    # if user's guessed letter was correct, here the program adds it to the correct operator above at line 12, if it was incorrect adds it to (incorrectguesses)
    if userguess in guess:
        correct.append(userguess)
        print("Nice guess, Go on!")
    else:
        incorrectguesses.append(userguess)
        print ("Sorry, the word doesn't contain", userguess,".")

def check():
    # A function to check to decide if the user wins or loses, if the operator (incorrectguesses) is above 6 which is 7 tries thats why i made it 6 then it displays,
    # a lossing message in line 57 else it returns winning message in line 60
    if len(incorrectguesses) > 6:
        return 'lose'
    for i in guess:
        if i not in correct:
            return 'loss'
    return 'winning'
# A while loop to rerun the program
while True:
    program()
    main()
    win_lose = check()
# The conditions that is checked from function check() before executing win/lose message
    if win_lose == 'lose':
        print ("GAME OVER!, your word was ",guess)
        break
    elif win_lose == 'winning':
        print("Coungratulations! You have won, your word was", guess)
        break