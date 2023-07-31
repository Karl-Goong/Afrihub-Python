import random





name = input("what is your name:")
decision = input(f'hi {name} would you like to play a game\n '
                 f'Y-for yes\n '
                 f'N-for no')

if(decision == 'Y'.lower()):
    print("That is nice. Lets Play!!\n "
          "Okay so this are the rules\n "
          "")

else:
    print("that sad. See you Next time")
    exit()

guess_limit = 3
guess_count = 0
guess_number = random.randint(1,10)


while guess_count<guess_limit:

    user_guess = input("Please Enter your number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please enter a number")
        continue


    if user_guess != guess_number:
        guess_count +=1
        print("please try again")
        if(user_guess>guess_number):
            print('the number is lower')
        elif(user_guess<guess_number):
            print("guess number is higher")
            if guess_count == guess_limit:
                print("sorry you ran out of guesses")

    elif user_guess == guess_number:
        print(f"congratulations {name}.. You guessed right after {guess_count+1} number of trials")
        break


# same program . make it more interactive


