#Milan Boga, Jack Chen

import random
#x is set to 0 so if it goes over 5 the game realises its done
x=0
#number 0-20
true_num= random.randint(0, 21)
a = 0
b = 20

#Function so if user wants to play game again
def play_game():
    while True:
        guess_num = int(input("Thank you for playing. You have 5 tries to guess a random number. Enter a number 0-20: "))
        while x < 4:
            if guess_num > true_num:
                x = x + 1
                print("Your guess was too high. Try again.")
                guess_num = int(input("Guess a number between " + a + "- " + b))
            elif guess_num < true_num:
                x = x + 1
                print("Your guess was too low. Try again.")
                guess_num = int(input("Guess a number between " + a + "- " + b))
            elif guess_num == true_num:
                print("You got it congratulations!")
                x = x + 5
                break
        if x == 5:
            print("Better luck next time")


while True:
    #the number you guess
    guess_num = int(input("Thank you for playing. You have 5 tries to guess a random number. Enter a number 0-20: "))
    while x < 4:
        #if number is to high
        if guess_num > true_num:
            x = x + 1
            print("Your guess was too high. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b))
        #if number is to low
        elif guess_num < true_num:
            x = x + 1
            print("Your guess was too low. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b))
        # if guessed number is correct
        elif guess_num == true_num:
            print("You got it congratulations!")
            x = x + 5
            break
    #once there 5 tries is up
    if x == 5:
        print("Better luck next time")
#if they want to play again
play_again = input('Want to play again? y/n: ')
if play_again == 'y':
        play_game()
elif play_again == 'n':
        print("Goodbye")
        