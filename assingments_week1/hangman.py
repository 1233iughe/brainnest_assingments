'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) 
to guess the correct letters before the game is over.
'''
from random import randint 
from string import ascii_letters

#Instructions to play the game
def introduction():
    print("Welcome to HangMan", 
          "You have 6 oportunities to guess the word.", 
          "Enter ONLY 1 letter per turn", 
          "Have fun!!!", 
          "\n",
          sep="\n")
    return None

#Prints how many tries the user has
def print_tries(tries):
    print(f"You have {tries} tries left.")
    return None

#Prints used letters 
def print_used_letters(used_letters):
    print(f"Used letters {' '.join(used_letters)}")
    return None

#Chosses a random word from the list
def word_chosser(word_list):
    return word_list[randint(0,len(word_list)-1)]

#Prints discovered word letters
def print_word(discovered_letters):
    print(f"Word: {' '.join(discovered_letters)}")
    return None

#Checks if letter is in word or in used_letters
def check_word(user_input, used_letters, discovered_letters, word):
    if user_input in used_letters:
        print(f"You have already used letter {user_input}, try another\n")
        return None
    
    for i in range(len(word)):
        if user_input == word[i]:
            discovered_letters[i] = user_input
            used_letters.append(user_input)

    return None

#Checks for faulty input from the user and reduce tries if input is acceptable
def input_checker():
    user_input = input("Guess a letter: ")
    if user_input:
        if len(user_input) == 1:
            if user_input in ascii_letters:
                print("\n")
                return user_input.lower()
            print("Only ascii letters allowed. Try again.\n")
            return 1

        print("Only 1 character allowed. Try again.\n")
        return 1
     
    print("Please provide input.\n")
    return 1

#Checks if player has won or lost
def game_over(tries, discovered_letters, word):
    if tries > 0:
        if ''.join(discovered_letters) == word:
            print(f"You guessed the word {word}!")
            return 0
        return 1
    print(f"You lost, the word was {word}!")
    return 0

#Main game loop
def game_loop():
    word_list = ['apple', 'banana', 'carrot', 'dog', 'cat', 'egg', 
                 'fish', 'goat', 'hand', 'kite', 'lion', 'moon', 
                 'nest', 'owl', 'pig', 'quail', 'rat', 'sun', 
                 'tiger', 'ant', 'bat', 'cow', 'duck', 'fox', 
                 'giraffe', 'hen', 'iguana', 'jelly', 'koala', 'llama']
    tries = 6
    used_letters = []
    switch = 1
    word = word_chosser(word_list)
    discovered_letters = ["_" for i in range(len(word))]

    while switch:
        print_tries(tries)
        print_used_letters(used_letters)
        print_word(discovered_letters)
        user_input = input_checker()
        if user_input != 1:
            tries -= 1
        check_word(user_input, used_letters, discovered_letters, word)
        switch = game_over(tries, discovered_letters, word)

    return 0


#Main function, all functionality is encapsulated here.
def main():
    introduction()
    game_loop()
    return 0

main()
# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''