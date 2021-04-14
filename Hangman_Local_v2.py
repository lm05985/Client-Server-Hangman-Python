#version 2
import random
#wordlist = ["planet","tree","random","free","holiday","notebook","school","simple","coding"]
word_chosen = ""
word_visualization = ""
max_guesses = 10
current_guesses_counter = 0
letters_guessed = []
current_guess = ""
j = 0
while True:
    word_chosen = input("Enter word to be guessed:")
    letters_guessed = len(word_chosen) * "_"
    current_guesses = 0
    print("Welcome to hangman!")
    print("You need to guess what word I am thinking of.")
    print("This word is ", len(letters_guessed), " letters")
    while current_guesses_counter-j < max_guesses:
        print("Guesses left: ",max_guesses-current_guesses_counter+j)
        current_guess = input("Enter a letter: ")
        print()
        for i in range(0, len(word_chosen)):
            if word_chosen[i] == current_guess:
                letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i+1:]
                print("You got a letter!")
                print(letters_guessed)
                print()
                j = j+1
        if word_chosen == letters_guessed:
            print("You won this time!")
            exit()
        current_guesses_counter+=1
    print("I got you this time, the word was:", word_chosen)
    exit()