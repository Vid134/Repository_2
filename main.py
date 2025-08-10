#Question 1: Guess the number

#firstly let us assume a random number between 1 to 50, here the computer selects the random number 
 #the player is the user who keeps guessing until find the correct number

import random # majorly used for generating random numbers,import is a module used in python
print("Guess the number : ")
secret_num = random.randint(1,50) #assigning secret number with the random integer between 1 to 50
guess = None #this will store guess
while guess != secret_num:  #keep asking until correct num is guessed
    guess = int(input("enter the guess between 1 and 50 : ")) #give input as a guess
    if guess < secret_num:  #if the guess is lesser than secret number ,it will show too low
        print("Too low! Try again")
    elif guess > secret_num:   #if the guess is higher than secret num , it will show too high
        print("Too high! Try again")
    else:      #if above both the conditions are false, this condition works
        print("Guess is correct!")


#hint: inorder to finf the secret_num ina easy way can add a code print(secret_num) after teh line8


#Question 2: Word Scramble

import random  #majorly used for generating random words,import is a module used in python


words = ["python","javascript","java","automation","pytest","guvi","selenium"] #list of words
original_word = random.choice(words) #choose a word from the above list
scrambled_word = '' .join(random.sample(original_word,len(original_word))) #scrambling a word

print("Word Scramble Game!")
print(f"Unscramble this word: {scrambled_word}")

guessing = input("Your guess :") #guessing the player's word
if guessing.lower() == original_word: 
    print("Correct! Well done") #if the guessed word is the original word then the correct should should display
else:              
    print("Wrong! The correct word was :", {original_word})  #else it shows incorrect word and displays the original one



