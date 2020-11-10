#Collaborators: Milan Boga, Jack Chen
import random
#Function so if user wants to play game again
def play_game(x,a,b,true_num):
    try:
        print("Thank you for playing. You have 5 tries to guess a random number. Enter a number " + str(a) + " -", str(b) + ": ")
        guess_num = int(input())
    except:
        print("Invalid input")
        print("Thank you for playing. You have 5 tries to guess a random number. Enter a number " + str(a) + " -", str(b) + ": ")
        guess_num = int(input())
    while x < 4:
        if guess_num > true_num:
            x = x + 1
            print("Your guess was too high. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b) + ": "))
        elif guess_num < true_num:
            x = x + 1
            print("Your guess was too low. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b) + ": "))
        elif guess_num == true_num:
            print("You got it congratulations!")
            x = x + 5
            break

        if x == 5:
            print("Better luck next time")

#x is set to 0 so if it goes over 5 the game realises its done
x=0
#number 0-20
a = int(input("Put in your lowest number: "))
b = int(input("Put in your highest number: "))

true_num = random.randint(a, b)

play_game(x,a,b,true_num)

#if they want to play again
while True:
    play_again = input('Want to play again? y/n: ')
    if play_again == 'y':
            play_game(x,a,b,true_num)
    elif play_again == 'n':
            print("Goodbye")
            break