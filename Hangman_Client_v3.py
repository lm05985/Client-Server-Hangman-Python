#HANGMAN CLIENT v3
# WORKS!!! USE THIS ONE
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name, this works on local machine
# host = "SERVER IP ADDRESS HERE"                #find this out from server
#host = socket.gethostbyname(socket.gethostname()) # could use this too
port = 12345                # Reserve a port for your service.
s.connect((host, port))     #connect to socket

# print("Host:",host)
print("\nThank you for connecting to Hangman Server")
print("You need to guess what word I am thinking of....")

print("Number of letters in word: ",end=" ")
num_letters = s.recv(1024).decode()            #Receives number of letters 
print(num_letters)


max_guesses = s.recv(1024).decode()            # recieve variables
s.close()                                      # had to close socket and open new
s = socket.socket()                            # so that would have two different variables
s.connect((host, port))
word_chosen = s.recv(1024).decode()             #receive variable 




###set up variables for game
#word_chosen = ""
word_visualization = ""
#max_guesses = recieved from server
current_guesses_counter = 0
letters_guessed = []
current_guess = ""
letters_guessed = len(word_chosen) * "_"
current_guesses = 0
correct_num_guesses = 0                                          #keeps track of correct number of guesses

while current_guesses_counter-correct_num_guesses < int(max_guesses):
    print("Guesses left: ",int(max_guesses)-current_guesses_counter+correct_num_guesses)
    current_guess = input("Enter a letter: ")
    print()
    for i in range(0, len(word_chosen)):
        if word_chosen[i] == current_guess:
            letters_guessed = letters_guessed[:i] + current_guess + letters_guessed[i+1:]
            print("You got a letter!")
            print(letters_guessed)
            print()
            correct_num_guesses= correct_num_guesses+1
    if word_chosen == letters_guessed:
        print("You won this time!")
        result = "client win"
        s.send(result.encode())
        s.send(str(current_guesses_counter+1).encode())   
        print("Socket Connection Closed")
        s.close()   
        exit()
    current_guesses_counter+=1
print("I got you this time, the word was:", word_chosen)
print('You guessed',current_guesses_counter,'times')
result = "client lose" 
s.send(result.encode())
print("Socket Connection Closed")
s.close()   
exit()