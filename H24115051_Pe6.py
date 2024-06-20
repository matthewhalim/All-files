import random # imports random module
alphabet = 'abcdefghijklmnopqrstuvwxyz' # we define alphabet as a placeholder for guessing the letters
random_albt = random.choice(alphabet) # now we can give the program to pick a letter from 'alphabet' to start the game
print(random_albt) # testing
guess = input("Guess the lowercase alphabet:") # user to input the letter they want to guess
guesses = [] # a empty list to count the numbers of guesses given by the user
while True: # to let the program loop continuously
    try: # incase of any errors we use try and except so the user guess a letter
        if guess == random_albt: #  if the user guess is the same as the generated letter
            guesses.append(guess) # we will append this to the guesses
            print("Congratulations! You guessed the alphabet {}".format(random_albt)) # print function to congratulate and also we user format to direct the random letter to be printed
            print("Number of tries:", len(guesses)) # we use len to count the number of tries by the user
            break # because we achive the correct letter, we now then break the loop
        elif guess > random_albt: # if user has a higher letter than the random generated letter
            guesses.append(guess) # we will append it to the guesses
            print("The alphabet you are looking for is alphabetically higher")
            guess = input("Guess the lowercase alphabet:") # we then give the user to guess again
        elif guess < random_albt:
            guesses.append(guess)
            print("The alphabet you are looking for is alphabetically lower")
            guess = input("Guess the lowercase alphabet:")

    except ValueError:
        guess = input("Please input an alphabet!!!!")

print('Histogram:')
x = 0 #intiial value for x
while x < 100: #loops as long as x is under 100
    histo = 0 #resets the histogram every 10 numbers
    x += 4 #makes it so the histogram is seperated every 4 letter
    for i in range(guesses): #for loop that iterates over all the values in the list

            histo += 1











