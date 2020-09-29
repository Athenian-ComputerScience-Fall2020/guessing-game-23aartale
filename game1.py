import random
x=0
true_num= random.randint(0, 21)

try:
    guess_num = int(input("Thank you for playing. You have 5 tries to guess a random number. Enter a number 0-20: "))
    if guess_num == str:
#I want it if it types an integer or a number larger than 20 to rerun the except but it doesnt work
        while x < 4:
            if guess_num > true_num:
                x = x + 1
                print("Your guess was too high. Try again.")
                guess_num = int(input("Guess a number between " + a + "- " + b ":"))
            elif guess_num < true_num:
                x = x + 1
                print("Your guess was too low. Try again.")
                guess_num = int(input("Guess a number between " + a + "- " + b ":"))
            elif guess_num == true_num:
                print("You got it congratulations!")
                x = x + 5
            else:
                print("Too bad you didnt guess it. Better luck next time!")
except:
    print("Please put a number between " + a + "- " + b ":")