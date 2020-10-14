import random
x=0
true_num= random.randint(0, 21)
a = 0
b = 20

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
    guess_num = int(input("Thank you for playing. You have 5 tries to guess a random number. Enter a number 0-20: "))
    while x < 4:
        if guess_num > true_num:
            x = x + 1
            print("Your guess was too high. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b))
        elif guess_num < true_num:
            x = x + 1
            print("Your guess was too low. Try again.")
            guess_num = int(input("Guess a number between " + str(a) + "- " + str(b))
        elif guess_num == true_num:
            print("You got it congratulations!")
            x = x + 5
            break
        if x == 5:
            print("Better luck next time")

play_again = input('Play again? y/n: ')
if play_again == 'y':
        play_game()
if play_again == 'n':
        print("Goodbye")
        