#HANGMAN SERVER v4
# WORKS!!! USE THIS ONE
#set up variables for socket
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name, this works on local machine
# host = socket.gethostbyname(socket.gethostname()) #host = xxx.xxx.x.x for razerrrr
port = 12345                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
print("Host:", host)
print("\nWaiting for a connection, Hangman Server Started....")
#server chooses word to be guessed by client


c, addr = s.accept()                                             # Establish connection with client.
print('Got connection from', addr)


print('**case sensitive! please enter in all lower case**\n')
word_chosen = input("Enter word to be guessed:") 
letters_guessed = len(word_chosen) * "_"
max_guesses = input("Enter the maximum amount of guesses allowed:")
while int(max_guesses)<len(word_chosen):
    print('\nERROR... please allow at least 1 guess for each letter')
    print('Currently the word you chose has',len(word_chosen),'letters')
    max_guesses = input("Enter the maximum amount of guesses allowed:")

# c.send(str(len(letters_guessed)).encode()) 
c.send(str(len(word_chosen)).encode('utf8'))                    # sends number of letters to be guessed

c.send(max_guesses.encode())                              # send max guesses 

#close socket and opens new socket so that can recieve new variable
c.close()
s = socket.socket()
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()   
# print('Got connection from', addr)   #had to close/open a new socket to send word_chosen and max_guesses in diff variables

c.send(word_chosen.encode())                                    # sends word chosen for loop 


print("Waiting for opponent...")
result = c.recv(1024).decode()

if result in ['client lose']:
    print("You won!")
    c.close()                                                        # Close the connection    
    print("Socket Connection Closed")
    print("\n*To play again please restart*")
    exit()
elif result in ['client win']:
    print("You lost :(")
    print('It took the opponent',end=" ")
    # print("Guesses it took to guess:",end=" ")
    print(c.recv(1024).decode(),end=" ")
    print('guesses')
    c.close()                                                        # Close the connection
    print("Socket Connection Closed")
    print("\n to play again please restart")
    exit()
