import random
x=0
true_num= random.randint(0, 21)
guess_num = int(input("Thank you for playing. You have 5 tries to guess a random number. Enter a number 0-20: "))
while x < 4:
    if guess_num > true_num:
        print("Your guess was too high. Try again.")
        guess_num = int(input("Enter a number 0-20: "))
        x = x + 1
    elif guess_num < true_num:
        print("Your guess was too low. Try again.")
        guess_num = int(input("Enter a number 0-20: "))
        x = x + 1
    else:
        print("You got it congratulations!")
        x = x + 5
        
print("Too bad you didnt guess it. Better luck next time!")